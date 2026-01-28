import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def print_news(index, title, link):
    print(f"{index+1}. {title}")
    print(f"  (링크: {link})")

def create_soup(url):
    headers  ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def create_selenium_soup(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    browser.maximize_window()
    browser.get(url)
    time.sleep(3)
    # 특정 요소가 나타날 때까지 최대 10초 대기
    # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.card_detail._cnBlockTemplate")))
    soup = BeautifulSoup(browser.page_source, "lxml")

    return soup


# [오늘의 날씨]
# 흐림, 어제보다 00℃ 높아요
# 현재 00℃ (최저 00℃ / 최고 00℃)
# 강수확률 00
# 미세먼지 00㎕/㎥ 좋음
# 초미세먼지 00㎕/㎥ 좋음
# 오전 강수확율 00% / 오후 강수확률 00%
def get_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=0&acr=1&ie=utf8&query=%EB%82%A0%EC%94%A8%EC%98%88%EB%B3%B4&ackey=mno9gc18"
    soup = create_soup(url)
    with open("files/weather.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())


    weather = soup.find("div", attrs={"class":"status_wrap"})
    today_temperature = weather.find("div", attrs={"class":"temperature_text"} ).get_text().replace("현재 온도","")
    temperature_updown = weather.find("span", attrs={"class":"temperature"} )
    blind = weather.find("span", attrs={"class":"blind"})
    print("find", weather.find("li", attrs={"class":"item_today level1"} ))
    fine_dust = weather.find("li", attrs={"class":"item_today level1"} ).find("span", attrs={"class":"txt"} )
    ultrafine_dust = weather.find("li", attrs={"class":"item_today level2"} ).find("span", attrs={"class":"txt"} )

    today_weather = soup.find("li", attrs={"class":"week_item today"})
    lowest = today_weather.find("span", attrs={"class":"lowest"})
    highest = today_weather.find("span", attrs={"class":"highest"})

    rain_rate_morning = today_weather.find_all("span", attrs={"class":"rainfall"} )[0]
    rain_rate_afternoon = today_weather.find_all("span", attrs={"class":"rainfall"} )[0]

    locate = soup.find("div", attrs={"class":"title_area _area_panel"}).find("h2", attrs={"class":"title"} ).get_text().strip()

    print("[오늘의 날씨]")
    print(f"{locate} 기준")
    print(f"{blind.get_text()}, 어제보다 {temperature_updown.get_text()}")
    print(f"{today_temperature.strip()} ( 최저 {lowest.get_text().replace("최저기온","")} / 최고 {highest.get_text().replace("최고기온","")} )")
    print(f"미세먼지 {fine_dust.get_text()}")
    print(f"초미세먼지 {ultrafine_dust.get_text()}")
    print(f"오전 강수확률 {rain_rate_morning.get_text()} / 오후 강수확률 {rain_rate_afternoon.get_text()}")
    print("="*100)

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

    with open("files/weather.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

    weather = soup.find("div", attrs={"class":"card card_detail _cnBlockTemplate"})

    weather_summary = weather.find("em", attrs={"class":"card_date_emphasis"} )
    today_temperature = weather.find("strong", attrs={"class":"card_now_temperature"} )
    low_high_temperature = weather.find_all("dd", attrs={"class":"card_description_data"})
    weather_description = weather.find("span", attrs={"class":"card_date_text type_down"} )
    fine_dust = weather.find("span", attrs={"class":"card_data_text level4_2"})
    ultrafine_dust = weather.find("span", attrs={"class":"card_data_text level4_1"})

    # print(weather)
    print("[오늘의 날씨]")
    print(f"{weather_summary.get_text().strip()}, {weather_description.get_text()}")
    print(f"{today_temperature.get_text()} (최저 {low_high_temperature[0].get_text()} / 최고 {low_high_temperature[1].get_text()})")
    print(f"미세먼지 {fine_dust.get_text()}")
    print(f"초미세먼지 {ultrafine_dust.get_text()}")
    print("="*100)

    browser.quit()

def get_headline_news():
    url = "https://media.naver.com/press/437"
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"class":"press_main_news_inner"}).find_all("li",attrs={"class":"press_news_item"}, limit=3)

    print("[오늘의 헤드라인 뉴스]")
    for index, news in enumerate(news_list):
        title = news.find("span", attrs={"class":"press_news_text"}).get_text().strip()
        link = news.find("a")["href"]

        print_news(index, title, link)

    print("="*100)

def get_it_news():
    url = "https://news.naver.com/section/105"
    soup = create_soup(url)
    # soup = create_selenium_soup(url)

    with open("../webscraping_project/files/weather.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

    # news_list = soup.find("ul", attrs={"id":re.compile(r"_SECTION_HEADLINE_LIST_")}).find_all("div", attrs={"class":"sa_text"}, limit=3)
    news_list = soup.find("div", attrs={"class":"section_article as_headline _TEMPLATE"}).find_all("div", attrs={"class":"sa_text"}, limit=3)
    # print(news_list)

    print("[IT 뉴스]")
    for index, news in enumerate(news_list):

        a_tag = news.find("a")
        title = a_tag.get_text().strip()
        link = a_tag["href"]

        print_news(index, title, link)

    print("="*100)

def get_english():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents_speaking/I_others_english&keywd=haceng_main_gnb_eng_I_others_english&logger_kw=haceng_main_gnb_eng_I_others_english"
    soup = create_soup(url)
    # sentence = soup.find_all("div", attrs={"class":"conv_txt"})
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print("[오늘의 영어 회화]")
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 가정 index 4~7
        print(sentence.get_text().strip())
    print()
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 가정 index 4~7
        print(sentence.get_text().strip())

    print("="*100)

if __name__ == "__main__":
    get_weather() # 오늘 날씨정보 가져오기 request 사용
    # get_today_weather() # 오늘 날씨정보 가져오기 selenium 사용
    get_headline_news() # 오늘 헤드라인 뉴스 가져오기
    get_it_news() # IT 뉴스 가져오기
    get_english() # 영어 회화 가져오기
