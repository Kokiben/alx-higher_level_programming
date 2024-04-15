#!/usr/bin/python3
""""Class definition for State"""
from sqlalchemy import Column, Integer, String
from model_state import Base


class State(Base):
    """A simple represention of a class State"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
