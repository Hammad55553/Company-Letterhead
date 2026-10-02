from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LetterRecordBase(BaseModel):
    letter_type: str
    recipient_name: str
    subject: str
    ref_no: str
    content: str

class LetterRecordCreate(LetterRecordBase):
    pass

class LetterRecordUpdate(BaseModel):
    content: Optional[str] = None
    recipient_name: Optional[str] = None

class LetterRecord(LetterRecordBase):
    id: int
    issue_date: datetime

    class Config:
        orm_mode = True
