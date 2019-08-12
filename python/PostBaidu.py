print(1)

#导入模块
import urllib.parse
import urllib.request

#将数据进行urlencecode编码处理后，再使用encoding设置为utf-8编码
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
reponse = urllib.request.urlopen("http://httpbin.org/post", data=data)
html = reponse.read()
print(html)