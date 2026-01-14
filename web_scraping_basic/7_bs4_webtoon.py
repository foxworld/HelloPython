from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    page.goto("https://comic.naver.com/webtoon", wait_until="domcontentloaded")
    page.wait_for_selector("span.ContentTitle__title--e3qXt")
    # 렌더링된 HTML 가져오기
    time.sleep(1)
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "lxml")
cartoons = soup.find_all("span", attrs={"class":"ContentTitle__title--e3qXt"})
for cartoon in cartoons:
    title = cartoon.find("span", attrs={"class":"text"})
    # print(title)
    name = title.get_text(strip=True)
    print(name)
