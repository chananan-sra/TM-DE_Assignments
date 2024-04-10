from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import get_db
from .models import Checkin

app = FastAPI()


def get_checkins_for_user(db: Session, user: str):
    return db.query(Checkin).filter(Checkin.user == user).all()


@app.get("/checkins")
async def get_checkins(user: str, db: Session = Depends(get_db)):
    checkins = get_checkins_for_user(db, user)
    return checkins
