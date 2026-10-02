from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
import datetime

class LetterRecord(Base):
    __tablename__ = "letter_records"

    id = Column(Integer, primary_key=True, index=True)
    letter_type = Column(String, index=True)
    recipient_name = Column(String, index=True)
    subject = Column(String)
    ref_no = Column(String)
    content = Column(Text)
    issue_date = Column(DateTime, default=datetime.datetime.utcnow)
