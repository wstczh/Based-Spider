import urllib.request
import urllib.parse

url="http://www.iqianyue.com/mypost"
mydata=urllib.parse.urlencode({
    "name":"517690078@qq.com",
    "pass":"1234534"
}).encode("utf-8")
req=urllib.request.Request(url,mydata)
data=urllib.request.urlopen(req).read()
with open("D:/python learning/result/3.html","wb") as f:
    f.write(data)