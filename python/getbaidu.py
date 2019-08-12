

import urllib.request       #导入模块
session =urllib.request.urlopen('https://www.baidu.com')        #打开指定需要爬取的网页
html = session.read()       #读取网页代码

print(html)         #打印指定内容