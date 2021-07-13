import requests
import re
import os

url = 'https://www.h128.com/pc/anime/0/2/1920x1080/t/1.html' #网页的网址

headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
} #加入请求头
r = requests.get(url,headers = headers) #get
r.raise_for_status()
r.encoding = r.apparent_encoding
#print(r.text)
a = re.findall('<img src="https:(.*?)" alt',r.text) #(.*?)表示任意的字符串
for i in a:
    #print(i)
    url = 'https:' + i
    url = url.replace('w_487', 'w_1421').replace('h_274', 'h_799')
    #print(x)
    r = requests.get(url,headers = headers)
    root = "D://pics1//"#保存在D盘的pics1里，这里要提前建好文件夹
    if not os.path.exists : 
        os.makedirs(root)
    path = root + url.split('?')[0].split('/')[-1] #图片的名字更改
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print("文件已保存成功")
