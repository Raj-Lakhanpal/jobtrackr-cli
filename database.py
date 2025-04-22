import sqlite3

def initialize_database():
    conn = sqlite3.connect("jobtrackr.db") # Create the DB file if it doesn't exist
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS jobs (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   company TEXT NOT NULL,
                   role TEXT NOT NULL,
                   status TEXT NOT NULL,
                   applied_date TEXT,
                   notes TEXT)
                   ''')
    conn.commit()
    conn.close()