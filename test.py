import requests
from bs4 import BeautifulSoup
import json

url = 'https://gz.meituan.com/'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'gz.meituan.com',
    'Referer':'http://gz.meituan.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
    'Content-Type':'text/html; charset=utf-8',
}

#获取主页源码
def get_start_links(url):
    html = requests.get(url).text   #发送请求 获取主页文本
    print(html)
start_url_list = get_start_links(url)
