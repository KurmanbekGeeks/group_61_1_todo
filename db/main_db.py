from config import path_db
from db import queries
import sqlite3


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.task_table)
    conn.commit()
    conn.close()
