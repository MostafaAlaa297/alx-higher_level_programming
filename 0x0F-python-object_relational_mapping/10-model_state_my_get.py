#!/usr/bin/python3

"""
Get state ids and names
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def main():
    """
    Main funtion
    """
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    my_session = sessionmaker(bind=engine)

    session = my_session()

    row = session.query(State).filter(State.name == sys.argv[4]).first()

    if (row):
        print("{}".format(row.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
