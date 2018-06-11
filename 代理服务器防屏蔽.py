import urllib.request
def use_proxy(url):
    proxy=urllib.request.ProxyHandler({"http":"122.114.31.177:808"})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    return data

url="http://www.baidu.com"
data=use_proxy(url)
print(len(data))