from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
import openai
from pydantic import BaseModel
from typing import Optional
from database import init_db, save_message, get_conversation_history, delete_conversation_db
from document_handler import process_document
from datetime import datetime

load_dotenv()

app = FastAPI(title="ChatGPT Clone", version="1.0.0")

# Models
class ChatRequest(BaseModel):
    conversation_id: str
    message: str
    theme: Optional[str] = "light"

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Store active conversations
conversations = {}
documents_context = {}

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()
    print("✓ ChatGPT Clone iniciado com sucesso")

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "app": "ChatGPT Clone",
        "version": "1.0.0"
    }

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY não configurado")
            
        conversation_id = request.conversation_id
        user_message = request.message
        theme = request.theme or "light"
        
        # Get conversation history from database
        history = get_conversation_history(conversation_id, limit=10)
        
        # Build system prompt
        system_prompt = """Você é um assistente de inteligência artificial útil e amigável.
        
Responda de forma clara, concisa e útil."""
        
        # Prepare messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history
        for msg in history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Add current message
        messages.append({"role": "user", "content": user_message})
        
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
        )
        
        assistant_message = response.choices[0].message.content
        
        # Save messages to database
        save_message(conversation_id, "user", user_message)
        save_message(conversation_id, "assistant", assistant_message)
        
        return {
            "conversation_id": conversation_id,
            "message": assistant_message,
            "theme": theme,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/upload-document")
async def upload_document(
    conversation_id: str,
    file: UploadFile = File(...)
):
    """Upload and process a document"""
    try:
        content = await file.read()
        
        # Process document based on type
        document_text = process_document(file.filename, content)
        
        # Store document context
        if conversation_id not in documents_context:
            documents_context[conversation_id] = []
        
        documents_context[conversation_id].append({
            "filename": file.filename,
            "content": document_text[:2000],  # Store first 2000 chars
            "timestamp": datetime.now().isoformat()
        })
        
        return {
            "status": "success",
            "filename": file.filename,
            "message": "Documento processado com sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get specific conversation"""
    try:
        history = get_conversation_history(conversation_id)
        return {
            "conversation_id": conversation_id,
            "messages": history,
            "documents": documents_context.get(conversation_id, [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/conversations/{conversation_id}")
async def delete_conversation(conversation_id: str):
    """Delete a conversation"""
    try:
        # Delete from database
        from database import delete_conversation_db
        delete_conversation_db(conversation_id)
        
        # Remove from memory
        if conversation_id in documents_context:
            del documents_context[conversation_id]
        
        return {"status": "success", "message": "Conversa deletada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../frontend/static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=False
    )
