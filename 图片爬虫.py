import urllib.request
import re
keyname="背心吊带"
key=urllib.request.quote(keyname)
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
for i in range(1,3):
    url="https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.5.5af911d9PzEM1G&q="+key+"&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&bcoffset=12&s="+str(i*60)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    pat='"picUrl":"//(.*?)"'
    pat2='"nick":"(.*?)"'
    imagelist=re.compile(pat).findall(data)
    shangjialist=re.compile(pat2).findall(data)
    for j in range(0,len(imagelist)):
        thisimg=imagelist[j]
        shangjia=shangjialist[j]
        thisimgurl="http://"+thisimg
        print(shangjia)
        # file="D:/python learning/result/taobao/"+str(i)+str(j)+".jpg"
        # urllib.request.urlretrieve(thisimgurl,file)
        with open("D:/python learning/result/11.txt","a") as f:
            f.write("店家"+shangjia+"的地址是："+thisimgurl+"\n")

