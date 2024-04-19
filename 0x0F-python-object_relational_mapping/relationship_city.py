#!/usr/bin/python3
"""
Class definition for a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    A simple represention of a city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    nam = Column(String(128), nullable=False)
    id_state = Column(Integer, ForeignKey("states.id"), nullable=False)
