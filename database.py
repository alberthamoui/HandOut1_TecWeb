import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:
    def __init__(self, DB_FILENAME) -> None:
        self.conn = sqlite3.connect('{}.db'.format(DB_FILENAME))
        self.conn.execute('CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)')
        self.conn.commit()


    def add(self, note):
        sql = "INSERT INTO note (title, content) VALUES (?, ?)"
        values = (note.title, note.content)
        self.conn.execute(sql, values)
        self.conn.commit()