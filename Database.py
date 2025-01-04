import sqlite3


def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

# Only initialize the database when this file is run directly
if __name__ == '__main__':
    init_db()
