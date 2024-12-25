# boiler plate file for models, designed to be use with SQLModel
# https://sqlmodel.tiangolo.com/
# For database migration and upgrade or version control, etc, use alembic in this tutorial written by kasper junge
# https://medium.com/@kasperjuunge/how-to-get-started-with-alembic-and-sqlmodel-288700002543

# Ps, everything should be works fine if you use sqlalchemy

# example, combination with Enum datatype

# from sqlmodel import SQLModel, Field
# from .enums import UserRole
#
#
# class User(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     username: str = Field(index=True)
#     email: str = Field(index=True)
#     role: UserRole = Field(default=UserRole.USER, index=True)
