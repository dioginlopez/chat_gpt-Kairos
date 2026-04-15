import json
import os
from datetime import datetime
from pathlib import Path

# Use JSON file for storage instead of SQLAlchemy
DB_FILE = "chatgpt.json"

def init_db():
    """Initialize database file"""
    if not os.path.exists(DB_FILE):
        initial_data = {
            "conversations": {},
            "messages": {}
        }
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)

def _load_db():
    """Load database from JSON file"""
    if not os.path.exists(DB_FILE):
        init_db()
    
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def _save_db(data):
    """Save database to JSON file"""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_message(conversation_id: str, role: str, content: str):
    """Save a message to database"""
    data = _load_db()
    
    # Ensure conversation exists
    if conversation_id not in data["conversations"]:
        data["conversations"][conversation_id] = {
            "id": conversation_id,
            "title": f"Conversa - {datetime.now().strftime('%d/%m/%Y')}",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
    
    if conversation_id not in data["messages"]:
        data["messages"][conversation_id] = []
    
    # Save message
    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    data["messages"][conversation_id].append(message)
    
    _save_db(data)

def get_conversation_history(conversation_id: str, limit: int = 10):
    """Get conversation history"""
    data = _load_db()
    
    messages = data["messages"].get(conversation_id, [])
    
    # Return last 'limit' messages in chronological order
    if len(messages) > limit:
        messages = messages[-limit:]
    
    return [
        {
            "role": msg.get("role"),
            "content": msg.get("content"),
            "timestamp": msg.get("timestamp")
        }
        for msg in messages
    ]

def delete_conversation_db(conversation_id: str):
    """Delete all messages from a conversation"""
    data = _load_db()
    
    # Remove conversation
    if conversation_id in data["conversations"]:
        del data["conversations"][conversation_id]
    
    # Remove messages
    if conversation_id in data["messages"]:
        del data["messages"][conversation_id]
    
    _save_db(data)

def get_all_conversations():
    """Get all conversations"""
    data = _load_db()
    return list(data["conversations"].values())
