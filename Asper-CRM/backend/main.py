from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models, schemas
from database import engine, SessionLocal

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Asper CRM API - SQLite Enabled")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Asper InfoTech CRM Backend"}

@app.post("/api/letters", response_model=schemas.LetterRecord)
def create_letter(letter: schemas.LetterRecordCreate, db: Session = Depends(get_db)):
    db_letter = models.LetterRecord(**letter.dict())
    db.add(db_letter)
    db.commit()
    db.refresh(db_letter)
    return db_letter

@app.get("/api/letters", response_model=List[schemas.LetterRecord])
def read_letters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    letters = db.query(models.LetterRecord).offset(skip).limit(limit).all()
    return letters

@app.put("/api/letters/{letter_id}", response_model=schemas.LetterRecord)
def update_letter(letter_id: int, letter: schemas.LetterRecordUpdate, db: Session = Depends(get_db)):
    db_letter = db.query(models.LetterRecord).filter(models.LetterRecord.id == letter_id).first()
    if not db_letter:
        raise HTTPException(status_code=404, detail="Letter not found")
    
    update_data = letter.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_letter, key, value)
        
    db.commit()
    db.refresh(db_letter)
    return db_letter
