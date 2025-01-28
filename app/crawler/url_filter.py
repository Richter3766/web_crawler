import sqlite3

from app import db_manager

class UrlFilter:
    def __init__(self, db_file):
        self.session = db_manager.get_session()
        self.db_file = db_file

    def filter_urls(self, urls: list[str], prefix):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        result = []
        for url in urls:
            if not url.startswith('https://'):
                url = prefix + url

            cursor.execute('SELECT url FROM url_table WHERE url = ?', (url,))
            rows = cursor.fetchall()
            if not rows:
                cursor.execute('INSERT INTO url_table (url) VALUES (?)', (url,))
                conn.commit()
                result.append(url)
        cursor.close()
        conn.close()
        return result
