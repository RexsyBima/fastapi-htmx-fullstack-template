# run this file to create database
import os  # TODO: -> check if database.db already exists, if exists, dont create database
from app.models import *
from sqlmodel import create_engine, SQLModel

# we use sqlite3 for simplicity
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)
# create tables
SQLModel.metadata.create_all(engine)
