import urllib.request
import re

data=urllib.request.urlopen("https://read.douban.com/provider/all").read()
data=data.decode("utf-8")
pat='<div class="name">(.*?)</div>'
mydata=re.compile(pat).findall(data)
with open("D:/python learning/title.txt","w") as f:
    for i in range(0,len(mydata)):
        f.write(mydata[i]+"\n")
print(mydata)
