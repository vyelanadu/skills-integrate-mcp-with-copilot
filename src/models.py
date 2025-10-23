from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from .db import Base


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    schedule = Column(String, nullable=True)
    max_participants = Column(Integer, default=0)
    # store participant emails as a simple JSON list for now
    participants = Column(JSON, default=list)
