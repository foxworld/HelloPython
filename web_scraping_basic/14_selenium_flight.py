import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window() # 창 최대화

def get_element(elems, target):
    result = []
    for elem in elems:
        try:
            b = elem.find_element(By.TAG_NAME, "b")
            if b.text.strip() == target:
                result.append(elem)
        except:
            pass

    print("찾은 개수:", len(result))
    return result


url = "https://flight.naver.com/flights/"
browser.get(url)
time.sleep(5)

browser.find_element(By.CSS_SELECTOR, '[data-event-area-code="rnd.depdate1"]').click()

elems = browser.find_elements(By.CSS_SELECTOR, ".sc-jlZhew.hTjJbq.inner")
es = get_element(elems, "26")
print(len(es), es)
if len(es) > 0:
    print(es[0].text, es[0].tag_name, es[0].get_attribute("innerHTML"))
    es[0].click()

time.sleep(5)

elems = browser.find_elements(By.CSS_SELECTOR, ".sc-jlZhew.hTjJbq.inner")
es = get_element(elems, "3")
print(len(es), es)
if len(es) > 0:
    print(es[1].text, es[1].tag_name, es[1].get_attribute("innerHTML"))
    es[1].click()
time.sleep(10)

elems = browser.find_elements(By.CSS_SELECTOR, "img[alt='제주']")
if len(elems) > 0:
    for i in range(len(elems)):
        print(elems[i].get_attribute("innerHTML"))

time.sleep(30)