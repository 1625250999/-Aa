

from requests_html import HTMLSession


session = HTMLSession()
r = session.get('http://www.baidu.com')

print(r.text)