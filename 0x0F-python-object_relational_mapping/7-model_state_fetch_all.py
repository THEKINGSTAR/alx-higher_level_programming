#!/usr/bin/python

"""
Script that lists all State objects from the database hbtn_0e_6_us
"""

import sys
from sqlalchemy.ext.declarative import declarative_bas
from sqlalchemy.orm import column_property
from sqlalchemy import select, fun
from sqlalchemy import Column, Intr, String, ForeignKey
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def lists_all_State(mysql_username, mysql_password, database_name):
    """
    lists all State objects from the database hbtn_0e_6_usa
    Results must be sorted in ascending order by states.id
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    """
    Your code should not be executed when imported
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    lists_all_State(mysql_username, mysql_password, database_name)
