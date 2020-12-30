
import logging
import os
import shutil
import time
# 引入字节编码
from urllib.parse import quote

import requests
# 引入beautifulsoup
from bs4 import BeautifulSoup

BASEWEB = 'https://www.zhzyw.com/zyts/zyzj/'
BASEDETAIL = 'https://www.zhzyw.com/'
websites = ['cs', 'cs/index_2.html', 'jl', 'jl/index_2.html', 'jl/index_3.html', 'jl/index_4.html', 'jl/index_5.html',
            'jl/index_6.html', 'jl/index_7.html', 'jl/index_8.html', 'jl/index_9.html', 'jl/index_10.html',
            'qj', 'qj/index_2.html', 'qj/index_3.html', 'qj/index_4.html', 'qj/index_5.html', 'qj/index_6.html',
            'wh', 'wh/index_2.html', 'wh/index_3.html', 'wh/index_4.html', 'lc', 'lc/index_2.html', 'lc/index_3.html',
            'lc/index_4.html', 'lc/index_5.html', 'lc/index_6.html', 'lc/index_7.html', 'lc/index_8.html', 'lc/index_9.html', 'lc/index_10.html',
            'mj', 'mj/index_2.html', 'mj/index_3.html', 'dz', 'dz/index_2.html', 'fz', 'fz/index_2.html',
            'fz/index_3.html', 'fz/index_4.html', 'hz', 'hz/index_2.html', 'hz/index_3.html', 'mhz', 'mhz/index_2.html',
            'mhz/index_3.html', 'slz', 'slz/index_2.html', 'xzd', 'xzd/index_2.html', 'xzd/index_3.html', 'cymz', 'cymz/index_2.html',
            'gz', 'gz/index_2.html'
            ]
headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Host':
            'www.zhzyw.com',
            'Connection':
            'keep-alive',
            'Cache-Control':
            'max-age=0',
        }
session = requests.Session()
session.get(url=BASEWEB, headers=headers)

for website in websites:
    location = BASEWEB + website
    print('正在爬取页面： ' + location)
    page = session.get(location, headers=headers)
    page_text = page.content.decode('gb2312', 'ignore')

    soup = BeautifulSoup(page_text, 'lxml')
    detail_soup = soup.find(name='div', attrs={'id': 'main'}).find(name='div', class_='ullist01')
    detail_urls = [url.attrs['href'] for url in detail_soup.find_all(name='a')]

    for detail_url in detail_urls:
        try:
            detail_url_all = BASEDETAIL + detail_url
            print('     正在爬取子页面： ' + detail_url_all)
            detail_page = session.get(detail_url_all, headers=headers)
            detail_page_text = detail_page.content.decode('gb2312', 'ignore')

            page_soup = BeautifulSoup(detail_page_text, 'lxml')
            page_soup_main = page_soup.find(name='div', attrs={'id': 'main'}).find(name='div', attrs={'id': 'left'})
            text_data = ''
            text_data = text_data + page_soup_main.find(name='h1').text + "。"
            page_soup_main = page_soup_main.find(name='div', attrs={'class': 'webnr'})
            text_data = text_data + page_soup_main.text
            text_data.replace("\n", " ")
            with open('data.txt', 'a', encoding='utf-8') as file:
                file.write(text_data)
                file.write('\n')
        except Exception:
            continue

