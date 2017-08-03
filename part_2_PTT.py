import requests
from bs4 import BeautifulSoup

class PTTParser():

    BASE_URL = 'https://www.ptt.cc'
    INDEX_URL = 'https://www.ptt.cc/bbs/{}/index.html'

    def __init__(self, forum):
        self.forum = forum
        self.posts = []
        self.next_page_url = PTTParser.BASE_URL
        self.page_num = 1

    def get_posts(self):
        if self.page_num == 1:
            url = PTTParser.INDEX_URL.format(str(self.forum))
        else:
            url = self.next_page_url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        articles = soup.find_all('div', 'r-ent')

        control = soup.find('div', 'btn-group-paging').find_all('a', 'btn')
        self.next_page_url = PTTParser.BASE_URL + control[1]['href']

        for article in articles:
            meta = article.find('div', 'title').find('a')
            title = meta.getText().strip()
            url = meta.get('href')

            content_response = requests.get('https://www.ptt.cc' + url)
            content_soup = BeautifulSoup(content_response.text, 'lxml')
            for div in content_soup.find_all('div', 'push'):
                div.extract()
            for span in content_soup.find_all('span', 'f2'):
                span.extract()
            content = content_soup.find('div', 'bbs-screen bbs-content').getText()

            date = article.find('div', 'date').getText()
            author = article.find('div', 'author').getText()

            self.posts.append({
                'date': date,
                'author': author,
                'title': title,
                'content': content,
                'forum': self.forum
            })

    def get_posts_next_page(self):
        self.page_num += 1
        self.get_posts()

