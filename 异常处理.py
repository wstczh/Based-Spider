import urllib.error
import urllib.request

try:
    urllib.request.urlopen("Http://www.douban.com")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)