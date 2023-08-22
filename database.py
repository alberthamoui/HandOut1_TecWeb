import sqlite3
class Database:
    def __init__(self, DB_FILENAME) -> None:
        self.conn = sqlite3.connect('{}.db'.format(DB_FILENAME))
        self.conn.execute('CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)')