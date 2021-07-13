import requests
import bs4
# 指定用户代理
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
headers = {'user-agent': user_agent}
r = requests.get("https://blog.csdn.net/weixin_42156897/article/details/94581362", headers = headers)
#修改读取的编码方式，因为charset="utf-8"，所以要修改成 "utf-8"，否则中文会乱码
r.encoding = 'utf-8'
#查看响应状态码
print(r.status_code)

# print(r.text)

#使用BeautifulSoup解析代码,并锁定页码指定标签内容
content = bs4.BeautifulSoup(r.content.decode("utf-8"), "html.parser")
element = content.find_all(id='recommendAdBox')
print(element)
