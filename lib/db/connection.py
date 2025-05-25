import sqlite3

def get_connection():
    CONN = sqlite3.connect('lib/db/articles.db')
    CONN.row_factory = sqlite3.Row
    return CONN

