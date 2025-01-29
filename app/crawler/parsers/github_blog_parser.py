import hashlib

from bs4 import BeautifulSoup
from requests import Response

from app.crawler.parsers import ContentParser
from app.dto import CrawledDto


def generate_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

class GithubBlogParser(ContentParser):
    def parse(self, data: Response):
        soup = BeautifulSoup(data.text, 'html.parser')
        try:
            title = soup.select_one("body > header > div > div > div > div > div > h1").text
            contents = soup.get_text(separator='\n', strip=True)
            urls = [a['href'] for a in soup.find_all('a', href=True)]
        except Exception as e:
            print("parser 에러: ", data.url, e)
            return None

        if not title or not contents:
            return None

        hash_target = ' '.join(title + contents)
        hash_digest = generate_hash(hash_target)

        return CrawledDto(title, contents, urls, hash_digest)
