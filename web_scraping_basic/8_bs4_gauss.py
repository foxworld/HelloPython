from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    page.goto("https://comic.naver.com/webtoon/list?titleId=799793&page=1", wait_until="domcontentloaded")
    page.wait_for_selector("span.EpisodeListList__title--lfIzU")
    # 렌더링된 HTML 가져오기
    time.sleep(1)
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "lxml")
#cartoons = soup.find_all("span", attrs={"class":"EpisodeListList__title--lfIzU"})
#cartoons = soup.find_all("a", attrs={"class":"EpisodeListList__link--DdClU EpisodeListList__visited--f3pYN"})
cartoons = soup.find_all("a", attrs={"class":"EpisodeListList__link--DdClU"})

for cartoon in cartoons:
    # print(cartoon)
    title = cartoon.span.get_text(strip=True)
    link = "https://comic.naver.com" + cartoon['href']
    print(title, link)

# 평점구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체점수 : ", total_rates)
try:
    print("평균점수 : ", total_rates / len(cartoons))
except ZeroDivisionError:
    print("평균점수 : ", 0.0)

