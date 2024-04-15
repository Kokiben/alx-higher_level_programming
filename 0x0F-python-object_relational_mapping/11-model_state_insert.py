#!/usr/bin/python3
""" State object with name passed as argument from database
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
    state_nw = State(name='Louisiana')
    sitting.add(state_nw)
    new_call = sitting.query(State).filter_by(name='Louisiana').first()
    print(new_call.id)
    sitting.commit()
