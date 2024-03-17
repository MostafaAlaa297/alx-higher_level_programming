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

    Session = sessionmaker(bind=engine)

    session = Session()

    obj = State(name="Louisiana")
    session.add(obj)
    session.commit()

    print(obj.id)

    session.close()


if __name__ == "__main__":
    main()
