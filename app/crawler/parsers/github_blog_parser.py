import hashlib

from bs4 import BeautifulSoup

from app.crawler.parsers import ContentParser
from app.dto.crawled_dto import CrawledDto


def generate_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

class GithubBlogParser(ContentParser):
    def parse(self, data):
        soup = BeautifulSoup(data.text, 'html.parser')

        title = soup.select("body > header > div > div > div > div > div > h1")[0].text
        contents = soup.select("body > main > div > div > ul.posts-list.list-unstyled")[0].text

        if not title or not contents:
            return None

        urls = [a['href'] for a in soup.find_all('a', href=True)]

        hash_target = ' '.join(title + contents)
        hash_digest = generate_hash(hash_target)

        return CrawledDto(title, contents, urls, hash_digest)
