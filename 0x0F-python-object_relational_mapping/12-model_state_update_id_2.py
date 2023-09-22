#!/usr/bin/python3

"""
Script script that changes the name of
a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import column_property
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import update


def update_State(mysql_username, mysql_password, database_name):
    """
    changes the name of a State object from the database hbtn_0e_6_usa
    Print the new states.id after creation
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    session = Session(engine)

    update_State = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(update_State)
    session.commit()
    session.close()


if __name__ == "__main__":
    """
    Your code should not be executed when imported
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    update_State(mysql_username, mysql_password, database_name)
