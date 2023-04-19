import enum


class RoleType(enum.Enum):
    simple_user = "simple_user"
    host = "host"
    admin = "admin"