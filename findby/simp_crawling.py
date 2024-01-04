# from bs4 import BeautifulSoup
# import requests
#
# # keyword=""&tab=products
#
# KREAM_URL = 'https://kream.co.kr/'
# response = requests.get(KREAM_URL)
#
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
import ssl

import requests
from bs4 import BeautifulSoup

kream_url = 'https://kream.co.kr/search?keyword=%EC%88%98%ED%94%84%EB%A6%BC%20%EB%82%98%EC%9D%B4%ED%82%A4'


def web_crawler(url):

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    # 헤더 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

    # 서버 응답 확인
    response = requests.get(url, headers=headers)

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, "html.parser")

    print(soup.prettify())


web_crawler(url=kream_url)
