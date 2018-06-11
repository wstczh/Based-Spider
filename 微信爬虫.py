#http://weixin.sougou.com
import re
import urllib.request
import time
import urllib.error

#自定义模块，功能为使用代理服务器爬一个网址
def use_proxy(proxy_addr,url):
    #建立异常处理机制
    try:
        # req=urllib.request.Request(url)
        # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36')
        # proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        # opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        # urllib.request.install_opener(opener)
        data=urllib.request.urlopen(url).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        #若为URLError一场，延时10秒执行
        time.sleep(5)
    except Exception as e:
        print("exception"+str(e))
        #若为Exception异常，延时1s执行
        time.sleep(1)

#设置关键词
key="Python"
#设置代理服务器
proxy="115.46.75.144：:8123"
#爬取多少页
for i in range(0,10):
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?query="+key+"&type=2&page="+str(i+1)
    thispagdata=use_proxy(proxy,thispageurl)
    print(len(str(thispagdata)))
    pat1='<a target="_blank" href="(.*?)"'
    #re.S可以匹配多行
    rs1=re.compile(pat1,re.S).findall(str(thispagdata))
    print(rs1)
    if(len(rs1)==0):
        print("此次("+str(i)+"页)没成功")
        continue
    for j in range(0,len(rs1)):
        thisurl=rs1[j]
        thisurl=thisurl.replace("amp;","")
        file="D:/python learning/result/Weixin/第"+str(i)+"页第"+str(j)+"篇文章.html"
        thisdata=use_proxy(proxy,thisurl)
        try:
            with open(file,"wb") as f:
                f.write(thisdata)
            print("第"+str(i)+"页第"+str(j)+"篇文章成功")
        except Exception as e:
            print(e)
            print("第"+str(i)+"页第"+str(j)+"篇文章失败")

