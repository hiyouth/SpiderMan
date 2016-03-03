import time
from io import BytesIO
import pycurl
from util import get_html, write

__author__ = 'bliss'


class Grabber:
    def __init__(self, resource):
        self.contents = ''
        self.resource = resource
        self.content = ''

    def get(self):
        spide_url = getattr(self.resource, 'spide_url')
        self.content = get_html(self.resource.spide_url)

    def write(self):
        time_stamp = str(time.time())+'.html'
        write(time_stamp, self.content)





