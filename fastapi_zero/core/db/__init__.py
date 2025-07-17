from .db import BaseDB
from .postgresql import PostgresDB

db: BaseDB = PostgresDB()
