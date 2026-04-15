from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ChatRequest(BaseModel):
    """Chat message request model"""
    conversation_id: str
    message: str
    theme: Optional[str] = "light"

class ChatResponse(BaseModel):
    """Chat message response model"""
    conversation_id: str
    message: str
    theme: str
    timestamp: str

class MessageData(BaseModel):
    """Individual message in conversation"""
    role: str  # "user" or "assistant"
    content: str
    timestamp: Optional[str] = None

class ConversationHistory(BaseModel):
    """Conversation history model"""
    conversation_id: str
    messages: List[MessageData]
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class DocumentData(BaseModel):
    """Document data model"""
    filename: str
    content: str
    timestamp: str
    size: int

class ThemeConfig(BaseModel):
    """Theme configuration"""
    name: str
    primary_color: str
    secondary_color: str
    text_color: str
    background_color: str
