#!/usr/bin/python3

"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import column_property
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


def lists_all_State(mysql_username, mysql_password, database_name):
    """
    lists the first State objects from the database hbtn_0e_6_usa
    Results must be sorted in ascending order by states.id
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    session = Session(engine)

    """
    states = session.query(State).order_by(State.id).all()
    if (states is None):
        print("Nothing ")
    else:
        for state in states:
            print(f"{state.id}: {state.name}")
            return
    """
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    """
    Your code should not be executed when imported
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    lists_all_State(mysql_username, mysql_password, database_name)
