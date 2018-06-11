import urllib.request
import re
url="http://blog.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#将opener添加为全局，这样urlopen都能伪装成浏览器了
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8")
pat='<a href="(https://blog.csdn.net/.*?)"'
result=re.compile(pat).findall(data)
print(result)
for i in range(0,len(result)):
    file="D:/python learning/result/CSDN/"+str(i)+".html"
    urllib.request.urlretrieve(result[i],filename=file)
    print("第"+str(i+1)+"次爬取成功")