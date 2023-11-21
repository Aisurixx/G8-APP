import sqlite3
from datetime import datetime

class DatabaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect("confessions.db")
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS confessions (id INTEGER PRIMARY KEY, username TEXT, confession TEXT, date TEXT)")
        self.conn.commit()

    def post_confession(self, username, confession):
        date = datetime.now().strftime("%Y-%m-%d")

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO confessions (username, confession, date) VALUES (?, ?,  ?)", (username, confession, date))
        self.conn.commit()

    def delete_confession(self, username):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM confessions WHERE username = ?", (username,))
        self.conn.commit()

    def get_all_confessions(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM confessions")
        return cursor.fetchall()
    
    def remove_anonymous_posts(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM confessions WHERE username = 'Anonymous'")
        self.conn.commit()
