#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Sitting = sessionmaker(bind=engine)
    sitting = Sitting()
    for call in sitting.query(State).order_by(State.id):
        print(call.id, call.name, sep=": ")
        for city_ct in call.cities:
            print("    ", end="")
            print(city_ct.id, city_ct.name, sep=": ")
