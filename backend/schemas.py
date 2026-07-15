from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class HCPCreate(BaseModel):
    name: str
    specialization: Optional[str] = None
    hospital: Optional[str] = None
    location: Optional[str] = None


class HCPResponse(HCPCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class InteractionCreate(BaseModel):
    hcp_id: int
    interaction_type: str
    interaction_date: date
    topics_discussed: Optional[str] = None
    sentiment: Optional[str] = None
    summary: Optional[str] = None
    follow_up_date: Optional[date] = None


class InteractionUpdate(BaseModel):
    interaction_type: Optional[str] = None
    interaction_date: Optional[date] = None
    topics_discussed: Optional[str] = None
    sentiment: Optional[str] = None
    summary: Optional[str] = None
    follow_up_date: Optional[date] = None


class InteractionResponse(InteractionCreate):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
class FollowUpCreate(BaseModel):
    follow_up_date: date    
class ChatRequest(BaseModel):
    message: str
class ChatResponse(BaseModel):
    response: str    