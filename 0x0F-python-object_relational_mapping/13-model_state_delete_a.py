#!/usr/bin/python3

"""
Script that deletes all State objects
with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import column_property
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import delete


def deletes_State(mysql_username, mysql_password, database_name):
    """
    deletes all State objects from the database hbtn_0e_6_usa
    with a name containing the letter 'a' from the database
    """

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)

    session = Session(engine)

    update_State = delete(State).where(State.name.like('%a%'))
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
    deletes_State(mysql_username, mysql_password, database_name)
