#!/usr/bin/python3
"""
Print a script creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Sitting = sessionmaker(bind=engine)
    sitting = Sitting()

    StateNew = State(name='California')
    CityNew = City(name='San Francisco')
    StateNew.cities.append(CityNew)

    sitting.add(StateNew)
    sitting.add(CityNew)
    sitting.commit()
