import requests
# 引入beautifulsoup
from bs4 import BeautifulSoup

BASEWEB = 'https://www.zhzyw.com/zyts/zytn/'
BASEDETAIL = 'https://www.zhzyw.com/'
websites = ['sf', 'sf/index_2.html', 'sf/index_3.html', 'sf/index_4.html',
            'bb', 'bb/index_2.html', 'bb/index_3.html', 'bb/index_4.html',
            'bb/index_5.html', 'bb/index_6.html', 'bb/index_7.html', 'bb/index_8.html',
            'xe', 'xe/index_2.html', 'wh', 'bj', 'bj/index_2.html', 'jc']
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
        with open('data.txt', 'a', encoding='utf-8') as file:
            file.write(text_data)
            file.write('\n')

