import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re
import time
import random
import pandas as pd

# url ="http://localhost:63342/HelloPython/web_scraping_basic/coupang.html"
# url = "C:/IdeaProjects/study/HelloPython/web_scraping_basic/coupang.html"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
# res = requests.get(url)
# print("status :", res.status_code)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# html = res.text

def human_scroll(page):
    # 사람처럼 천천히 스크롤
    for _ in range(random.randint(5, 10)):
        page.mouse.wheel(0, random.randint(300, 800))
        time.sleep(random.uniform(0.5, 1.5))

item_list=[]
for i in range(1, 6):
    url = f"https://www.coupang.com/np/search?component=&q=%EC%95%84%EC%9D%B4%ED%8F%B0&traceId=mkeqe7zd&channel=user&page={i}"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            extra_http_headers={"Accept-Language": "ko-KR,ko;q=0.9",}
        )
        page = context.new_page()

        # webdriver 탐지 우회
        page.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")
        time.sleep(random.uniform(1.5, 3.0))
        page.goto(url)
        page.wait_for_selector("img", timeout=60000)

        # 사람처럼 스크롤
        human_scroll(page)

        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")
    items = soup.find_all("li", attrs={"class":re.compile("ProductUnit_productUnit*")})

    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("div", attrs={"class":re.compile("AdMark*")})
        if ad_badge:
            ad_badge="광고"
        else:
            ad_badge=""

        # print(item.find("div", attrs={"class":re.compile("ProductUnit_productNameV2*")}))
        name = item.find("div", attrs={"class":re.compile("ProductUnit_productNameV2*")}).get_text(strip=True)
        price = item.find("div", attrs={"class":re.compile("custom-oos fw-text*")}).get_text(strip=True)
        rate = item.find("div", attrs={"class":re.compile("fw-inline-flex fw-gap*")})
        link = item.find("a")['href'].strip()
        if rate:
            rate = item.find("div", attrs={"class":re.compile("fw-inline-flex fw-gap*")})['aria-label'].strip()
            print(type(rate))
        else:
            rate = "평점없음"
        review_tag = item.find("span", attrs={"class":re.compile("fw-inline-block fw-translate-y*")})
        if review_tag:
            review_count = re.compile(r'\d+').findall(review_tag.get_text(strip=True))
        else:
            review_count = "0"

        # 광고제외
        if ad_badge=="광고":
            continue
        # 리뷰 100개 이상, 평점 4,5되는 것만 조회
        if rate=="평점없음":
            continue
        elif float(rate) < 4.5:
            continue
        if float(review_count) <= 100:
            continue
        if "Apple" in name:
            continue
        print(ad_badge, name, price, rate, review_count, link)
        item_list.append([ad_badge, name, price, rate, review_count, link])
        print(f"제품명 : {name}")
        print(f"가격 : {price}")
        print(f"평점 : {rate}점 ({review_count})개")
        print(f"링크 : https://www.coupang.com{link}")

# df = pd.DataFrame(item_list, columns=['광고','상품명','가격','평점'])
# print(df)
