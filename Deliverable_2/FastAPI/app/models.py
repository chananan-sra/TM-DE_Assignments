from sqlalchemy import Column, String, DateTime, Float, Integer

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Checkin(Base):
    __tablename__ = "daily_checkins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String)
    timestamp = Column(DateTime(timezone=True))
    hours = Column(Float)
    project = Column(String)
