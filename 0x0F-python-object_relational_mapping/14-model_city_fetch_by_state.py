#!/usr/bin/python3
""" State object with name passed as argm from database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sitting = sessionmaker(bind=engine)
    sitting = Sitting()
    for call in (sitting.query(State.name, City.id, City.name)
                 .filter(State.id == City.state_id)):
        print(call[0] + ": (" + str(call[1]) + ") " + call[2])
