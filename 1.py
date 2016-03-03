import StringIO
import pycurl

c = pycurl.Curl()
str = StringIO.StringIO()
c.setopt(pycurl.URL, "http://t.cn/aKln8T")
c.setopt(pycurl.WRITEFUNCTION, str.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)

c.perform()
print(c.getinfo(pycurl.EFFECTIVE_URL))