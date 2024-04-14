#!/usr/bin/python3
""""Class definition for State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """A simple represention of a class State"""

     __tablename__ = "states"
    id = Column(Integer, primar_key=True)
    name = Column(String(128), nullstring=False)
