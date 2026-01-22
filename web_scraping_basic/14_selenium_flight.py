import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window() # 창 최대화

def get_element(elems, target):
    for elem in elems:
        if elem.find_element(By.TAG_NAME, "B").text.strip() == target:
            break
    return elem

url = "https://flight.naver.com/flights/"
browser.get(url)
browser.find_element(By.CSS_SELECTOR, '[data-event-area-code="rnd.depdate1"]').click()
time.sleep(5)

elems = browser.find_elements(By.CSS_SELECTOR, ".sc-jlZhew.hTjJbq.inner")
elem = get_element(elems, "26")
print(elem.text)
elem.click()

elems = browser.find_elements(By.CSS_SELECTOR, ".sc-jlZhew.hTjJbq.inner")
elem = get_element(elems, "31")
print(elem.text)
elem.click()

time.sleep(100)