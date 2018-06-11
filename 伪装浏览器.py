import urllib.request

url="http://blog.csdn.net/weiwei_pig/article/details/52123738"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
with open("D:/python learning/result/4.txt","wb") as f:
    f.write(data)