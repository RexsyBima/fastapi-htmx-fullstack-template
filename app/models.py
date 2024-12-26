# boiler plate file for models, designed to be use with SQLModel
# https://sqlmodel.tiangolo.com/
# For database migration and upgrade or version control, etc, use alembic in this tutorial written by kasper junge
# https://medium.com/@kasperjuunge/how-to-get-started-with-alembic-and-sqlmodel-288700002543

# Ps, everything should be works fine if you use sqlalchemy

# example, combination with Enum datatype

from sqlmodel import SQLModel, Field, create_engine, Session

from .enums import UserRole
sqlite_filename = "database.db"
sqlite_url = "sqlite:///" + sqlite_filename


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str = Field()
    email: str = Field(index=True)
    role: UserRole = Field(default=UserRole.USER, index=True)


engine = create_engine(sqlite_url, echo=True)
session = Session(engine)
