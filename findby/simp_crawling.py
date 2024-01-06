from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

KREAM_URL = 'https://kream.co.kr/search?keyword= '


def __simp_web_driver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    return webdriver.Chrome(options=chrome_options)


def simp_crawling(words: str) -> str:
    driver = __simp_web_driver()
    driver.get(KREAM_URL + words)
    try:
        result = driver.find_element(By.CLASS_NAME, "item_inner").text
    except NoSuchElementException:
        result = None
    finally:
        driver.quit()

    return result
