"""
需求：将新浪新闻首页(http://news.sina.com.cn/)中所有新闻都爬取到本地
思路：先爬取首页，通过正则获取所有新闻链接，然后依次爬取各种新闻，并存储到本地
"""
import urllib.request
import re
import urllib.error

data=urllib.request.urlopen("http://news.sina.com.cn/").read().decode("utf-8")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data)
for i in range(0,len(allurl)):
    try:
        print("这是第"+str(i)+"次爬取")
        thisurl=allurl[i]
        file="D:/python learning/result/sinanews/"+str(i)+".html"
        #将对应的url内容写到本地文件中
        urllib.request.urlretrieve(thisurl,file)
        print("--------爬取成功-------")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
