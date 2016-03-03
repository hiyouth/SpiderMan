from io import BytesIO
import pycurl
__author__ = 'bliss'


def get_html(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    # code = c.getinfo(c.HTTP_CODE)
    body = buffer.getvalue()
    c.close()
    return body.decode('utf-8')


def write(file_path, content):
    # 这里必须标注'utf-8', 否则会乱码
    file = open(file_path, 'w', -1, 'utf-8')
    file.write(content)
    file.close()
