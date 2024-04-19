#!/usr/bin/python3
"""
Class definition for a State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, MetaData

mimetadata = MetaData()
Base = declarative_base(metadata=mimetadata)


class State(Base):
    """
    A simple represention of a state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
