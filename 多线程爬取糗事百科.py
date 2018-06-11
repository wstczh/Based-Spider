import re
import urllib.request
import time
import urllib.error
import threading

# #设置A为线程
# class A(threading.Thread):
#     def __init__(self):
#         #初始化线程
#         threading.Thread.__init__(self)
#
#     def run(self):
#         for i in range(0,10):
#             print("我是线程A")
#
# # 设置B为线程
# class B(threading.Thread):
#     def __init__(self):
#         # 初始化线程
#         threading.Thread.__init__(self)
#
#     def run(self):
#         for i in range(0, 10):
#             print("我是线程B")
#
# t1=A()
# t1.start()
# t2=B()
# t2.start()

headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

class One(threading.Thread):
    def __init__(self):
        #初始化线程
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1,36,2):
            url = "https://www.qiushibaike.com/8hr/page/" + str(i)
            print(url)
            pagedata = urllib.request.urlopen(url).read().decode("utf-8")
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            print(datalist)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j + 1) + "个段子的内容是:")
                print(datalist[j])

class Two(threading.Thread):
    def __init__(self):
        #初始化线程
        threading.Thread.__init__(self)

    def run(self):
        for i in range(0,36,2):
            url = "https://www.qiushibaike.com/8hr/page/" + str(i)
            print(url)
            pagedata = urllib.request.urlopen(url).read().decode("utf-8")
            pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist = re.compile(pat, re.S).findall(pagedata)
            print(datalist)
            for j in range(0, len(datalist)):
                print("第" + str(i) + "页第" + str(j + 1) + "个段子的内容是:")
                print(datalist[j])

t1=One()
t2=Two()
t1.start()
t2.start()

