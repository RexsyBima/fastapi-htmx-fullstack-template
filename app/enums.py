# special file to define enums data, example below
from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    STAFF = "staff"
    USER = "user"
