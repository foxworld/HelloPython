import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)
browser.find_element(By.XPATH, "//*[@id='__next']/div/main/div[3]/div/div/div[2]/div[2]/button[1]").click()

# 이번달 27일 28일 선택
browser.find_elements(By.LINK_TEXT, "27")[0].click()
browser.find_elements(By.LINK_TEXT, "28")[0].click()


time.sleep(100)