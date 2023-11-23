#!/usr/bin/python3

"""
Script to define a SQLAlchemy model for a 'states' table in a MySQL database.

This script defines a SQLAlchemy model named 'State', which represents a table
named 'states' in a MySQL database. The table has two columns: 'id' as the
primary key (an integer that cannot be null) and 'name' as a string with a
maximum length of 128 characters (cannot be null). The script creates an
SQLAlchemy Engine to connect to a MySQL database and uses it to create the
'states' table.

Make sure to replace the database connection details (username, password,
database name) in the 'create_engine' line before running the script.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """Commentaire class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
