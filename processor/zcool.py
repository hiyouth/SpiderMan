from bs4 import BeautifulSoup
from util import write

__author__ = 'bliss'


class ZCool:
    def __init__(self):
        pass

    @staticmethod
    def parse_article_list(html):
        bfs = BeautifulSoup(html, 'lxml')
        total_list_tags = str(bfs.ul)
        write('dddd.html', total_list_tags)

    @staticmethod
    def parse_article(self):
        pass

