from enum import Enum

class DatabaseName(str, Enum):
    MYDATABASE = "mydatabase"
    ADMIN = "admin"
    LOCAL = "local"

class CollectionName(str,Enum):
    PROJECTS = "projects"

    