#!/usr/bin/python3

"""
Script that adds the State objecti 'Louisiana' to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import column_property
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


def lists_all_State(mysql_username, mysql_password, database_name):
    """
    insert State objects 'Louisiana' in the database hbtn_0e_6_usa
    Print the new states.id after creation
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    session = Session(engine)

    state_in = State(name='Louisiana')
    session.add(state_in)
    session.commit()

    print(state_in.id)
    session.commit()

    session.close()


if __name__ == "__main__":
    """
    Your code should not be executed when imported
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    lists_all_State(mysql_username, mysql_password, database_name)
