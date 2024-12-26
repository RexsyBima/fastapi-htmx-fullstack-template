# run this file to create database
import os
from app.models import *
from sqlmodel import create_engine, SQLModel

if os.path.exists("database.db"):
    raise Exception("database.db already exists")

# we use sqlite3 for simplicity
sqlite_filename = "database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)
# create tables
SQLModel.metadata.create_all(engine)
