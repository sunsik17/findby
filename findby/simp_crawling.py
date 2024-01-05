import ssl

import requests
from bs4 import BeautifulSoup

KREAM_URL = 'https://kream.co.kr/search?keyword=나이키 수프림'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

response = requests.get(KREAM_URL, headers=headers)

# 요청이 성공한 경우
if response.status_code == 200:
    # HTML을 파싱하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # 원하는 데이터가 포함된 스크립트 찾기
    script_tag = soup.find('script', text=lambda text: 'window.__NUXT__' in text)

    # 스크립트에서 데이터 추출
    if script_tag:
        script_content = script_tag.text
        # 데이터 처리 또는 정규표현식을 사용하여 원하는 부분 추출
        print(script_content)
        start_index = script_content.find('window.__NUXT__') + len('window.__NUXT__')
        end_index = script_content.find(';', start_index)
        data_str = script_content[start_index:end_index]

        # 데이터를 파이썬 객체로 변환 (예: JSON)
        # import json
        # data = json.loads(data_str)

        print(data_str)
    else:
        print("스크립트가 없거나 원하는 데이터를 찾을 수 없습니다.")
else:
    print(f"요청 실패: {response.status_code}")


# def search_by_words(url, words):
#
#     params = words.replace(' ', '%20')
#
#     if hasattr(ssl, '_create_unverified_context'):
#         ssl._create_default_https_context = ssl._create_unverified_context
#
#     # 헤더 설정
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#     }
#
#     # 서버 응답 확인
#     response = requests.get(url+params, headers=headers)
#
#     # BeautifulSoup 객체 생성
#     soup = BeautifulSoup(response.text, "html.parser")
#     # products = soup.select("#__layout > div > div.shop_mobile.content > div:nth-child(4)")
#     # print(products)
#     print(soup.prettify())
#     # print(soup.prettify().split("list_display_type")[1])
#     # document.querySelector(
#     #     "#__layout > div > div.shop_mobile.content > div:nth-child(4) > div:nth-child(1) > div.feeds.search_result.sm > div.search_result_list > div:nth-child(1) > a")
#
# search_by_words(url=KREAM_URL, words="나이키 수프림")
