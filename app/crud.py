from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas


VALID_STATUS_FLOW = {
    "Open": ["In Progress"],
    "In Progress": ["Closed"],
    "Closed": []
}

def create_bug(db: Session, bug: schemas.BugCreate):
    new_bug = models.Bug(
        title=bug.title,
        description=bug.description,
        priority=bug.priority,
        status="Open"
    )
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug


def get_bugs(db: Session):
    return db.query(models.Bug).all()

def update_bug(db: Session, bug_id: int, updates: schemas.BugUpdate):
    bug = db.query(models.Bug).filter(models.Bug.id == bug_id).first()
    if not bug:
        return None

    if updates.status:
        if updates.status not in VALID_STATUS_FLOW[bug.status]:
            raise ValueError("Invalid status transition")

    for field, value in updates.dict(exclude_unset=True).items():
        setattr(bug, field, value)

    bug.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(bug)
    return bug
