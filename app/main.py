from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bug Tracker API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/bugs", response_model=schemas.BugResponse)
def create_bug(bug: schemas.BugCreate, db: Session = Depends(get_db)):
    return crud.create_bug(db, bug)

@app.get("/bugs", response_model=list[schemas.BugResponse])
def list_bugs(db: Session = Depends(get_db)):
    return crud.get_bugs(db)

@app.put("/bugs/{bug_id}", response_model=schemas.BugResponse)
def update_bug(bug_id: int, updates: schemas.BugUpdate, db: Session = Depends(get_db)):
    try:
        bug = crud.update_bug(db, bug_id, updates)
        if not bug:
            raise HTTPException(status_code=404, detail="Bug not found")
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

