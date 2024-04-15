#!/usr/bin/python3
"""First State object from database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Sitting

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    sitting = Sitting(engine)
    call = sitting.query(State).order_by(State.id).call()
    if call:
        print("{}: {}".format(call.id, call.name))
    else:
        print("Nothing")
    sitting.close()
