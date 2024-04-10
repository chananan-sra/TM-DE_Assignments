from sqlalchemy import Column, String, TIMESTAMP, Float, Integer, DateTime, func

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Checkin(Base):
    __tablename__ = "daily_checkins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String)
    timestamp = Column(TIMESTAMP)
    hours = Column(Float)
    project = Column(String)
