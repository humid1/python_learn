import requests
import bs4

def get_html(url) :
    session = requests.Session()
    # 使用 requests 来发送请求
    start_html = session.get(url)
    soup = bs4.BeautifulSoup(start_html.content.decode("utf-8"), "html.parser")
    print(soup)

get_html("https://baidu.com")   