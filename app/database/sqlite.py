import sqlite3


def create_url_table(db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS url_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()


def clear_data_table(table: str, db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute(f'DELETE FROM {table}')

    conn.commit()
    conn.close()

