from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BugCreate(BaseModel):
    title: str
    description: str
    priority: str

class BugUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None



class BugResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True  
    }

