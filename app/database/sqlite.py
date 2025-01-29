import pickle
import queue
import sqlite3


def create_url_table(db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE,
            url_prefix TEXT NOT NULL
        )
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_url_prefix ON urls (url_prefix);')

    conn.commit()
    conn.close()


def create_queue_table(db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queues (
            queue_name TEXT,
            data BLOB
        )
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_queue_name ON queues (queue_name);')

    conn.commit()
    conn.close()

def clear_data_table(table_name: str, db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute(f'DELETE FROM {table_name}')

    conn.commit()
    conn.close()


def save_queue_to_db(queue_name, q, db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM queues WHERE queue_name = ?', (queue_name,))

    while not q.empty():
        data = q.get()
        serialized_data = pickle.dumps(data)
        cursor.execute('INSERT INTO queues (queue_name, data) VALUES (?, ?)', (queue_name, serialized_data))

    conn.commit()
    conn.close()


def load_queue_from_db(queue_name, db_file='crawler.db'):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    q = queue.Queue()

    cursor.execute('SELECT data FROM queues WHERE queue_name = ?', (queue_name,))
    rows = cursor.fetchall()

    for row in rows:
        data = row[0]
        try:
            deserialized_data = pickle.loads(data)
            q.put(deserialized_data)
        except Exception as e:
            print("역직렬화 에러 발생, 원인: ", e)

    conn.close()
    return q