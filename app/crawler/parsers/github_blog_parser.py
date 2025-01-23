import hashlib

from bs4 import BeautifulSoup

from app.crawler.parsers import ContentParser

def generate_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

class GithubBlogParser(ContentParser):
    def parse(self, contents):
        soup = BeautifulSoup(contents.text, 'html.parser')

        title = soup.select("body > header > div > div > div > div > div > h1")[0].text
        contents = soup.select("body > main > div > div > ul.posts-list.list-unstyled")[0].text

        hash_target = ' '.join(title + contents)
        hash_digest = generate_hash(hash_target)

        # TODO: redis나 메모리 활용하여 중복 검증

        # TODO: 중복 되지 않으면 url, date 등 데이터 파싱
        urls = [a['href'] for a in soup.find_all('a', href=True)]

        # TODO: 파싱된 데이터 다른 스레드로 전송
