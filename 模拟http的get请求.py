import urllib.request

keyword=input("请输入你想要查询的东西：")
#解决中文编码问题
keyword=urllib.request.quote(keyword)
url="http://www.baidu.com/s?wd="+keyword
#将url封装成一个请求
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
with open("D:/python learning/result/2.html","wb") as f:
    f.write(data)