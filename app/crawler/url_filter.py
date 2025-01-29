import sqlite3

class UrlFilter:
    def __init__(self, db_file='crawler.db'):
        self.db_file = db_file

    def filter_urls(self, urls: list[str], prefix):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        result = []
        for url in urls:
            if not url.startswith('https://'):
                url = prefix + url

            cursor.execute('SELECT url FROM urls WHERE url = ?', (url,))
            rows = cursor.fetchall()
            if not rows:
                url_prefix = url[:100]
                cursor.execute('INSERT INTO urls (url, url_prefix) VALUES (?, ?)', (url, url_prefix))
                result.append(url)

        conn.commit()
        conn.close()
        return result
