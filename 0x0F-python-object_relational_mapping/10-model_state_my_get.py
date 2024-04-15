#!/usr/bin/python3
""" State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sitting = sessionmaker(bind=engine)
    sitting = Sitting()
    call = sitting.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(call[0].id)
    except IndexError:
        print("Not found")
