import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# [오늘의 날씨]
# 흐림, 어제보다 00℃ 높아요
# 현재 00℃ (최저 00℃ / 최고 00℃)
# 강수확률 00
# 미세먼지 00㎕/㎥ 좋음
# 초미세먼지 00㎕/㎥ 좋음
def get_weather():
    url = "https://search.naver.com/search.naver?where=m&sm=mtb_drt&query=%EB%82%A0%EC%94%A8&ssc=tab.m.all"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    weather = soup.find("div", attrs={"class":"status_wrap"})
    today_weather_temperature = weather.find("div", attrs={"class":"temperature_text"} ).get_text()
    today_weather_expressions = weather.find("span", attrs={"class":"weather before_slash"} ).get_text()
    summary = weather.find("p", attrs={"class":"summary"} )
    temperature_up = weather.find("span", attrs={"class":"temperature up"} )
    blind = weather.find("span", attrs={"class":"blind"})

    print(weather)

    print("[오늘의 날씨]")
    print(f"{blind.get_text()}, 어제보다 {temperature_up.get_text()}")
    print(f"{today_weather_temperature.strip()} (최저 00℃ / 최고 00℃)")


def get_today_weather():
    url = "https://weather.naver.com/today/09650510?cpName=KMA"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    browser.maximize_window()
    browser.get(url)
    time.sleep(3)
    # 특정 요소가 나타날 때까지 최대 10초 대기
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.card_detail._cnBlockTemplate")))

    soup = BeautifulSoup(browser.page_source, "lxml")

    with open("weather.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

    weather = soup.find("div", attrs={"class":"card card_detail _cnBlockTemplate"})
    print(weather)

    browser.quit()

if __name__ == "__main__":
    # get_weather() # 오늘 날씨정보 가져오기
    get_today_weather()
