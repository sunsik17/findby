from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from findby.schemas import ProductDto

KREAM_URL = 'https://kream.co.kr/search?keyword= '


def __simp_web_driver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def simp_crawling(words: str, category: str) -> ProductDto:
    driver = __simp_web_driver()
    driver.get(KREAM_URL + words + category)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        result = driver.find_element(By.CLASS_NAME, "item_inner").text.split("\n")
        result.append(category)
        result.append("https://kream.co.kr" + soup.select_one(".item_inner")["href"])
    except NoSuchElementException:
        result = None
    finally:
        driver.quit()

    length = len(result)
    brand = result[1]
    name = result[2]
    if length > 8:
        amount = result[5]
    else:
        amount = result[4]
    category = result[length - 2]
    link = result[length - 1]
    return ProductDto(name=name, brand=brand, price=amount, category=category, link=link)
