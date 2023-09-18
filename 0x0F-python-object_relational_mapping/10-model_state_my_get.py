#!/usr/bin/python3

"""
Script  that prints the State object with the 'name'
passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import column_property
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


def lists_name_State(mysql_username, mysql_password, database_name, name_search):
    """
    prints the State object with the 'name'
    passed as argument from the database hbtn_0e_6_usa
    Results must be sorted in ascending order by states.id
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name==name_search)\
             .first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    """
    Your code should not be executed when imported
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    name_search = sys.argv[4]

    lists_name_State(mysql_username, mysql_password, database_name, name_search)
