#!/usr/bin/python3

"""
MODULE contains the class definition of a State
and an instance Base = declarative_base()
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Unicode
from sqlalchemy.orm import relationship

from model_state import Base

Base = declarative_base()


class State (Base):
    """
    Class state inheret from base to map the object
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id', ondelete='CASCADE'),nullable=False)

    def __repr__(self):
        return ("{} {}".format(self.id, self.name))


if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_url = "mysql://{}:{}@localhost:3306/{}"\
             .format(mysql_username, mysql_password, database_name)
    engine = create_engine(db_url)

    Base.metadata.create_all(engine)
