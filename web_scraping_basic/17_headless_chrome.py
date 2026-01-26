from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # 최신 headless 모드
options.add_argument("--window-size=1920,1080")
# options.headless = True
# options.add_argument("window-size=1920x1080")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
import time
interval = 2 # 2초에 한 번씩 스크롤 내리기

url = "https://play.google.com/store/books"
browser.get(url)

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
# 반복수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
    print("scrolling...: ", prev_height, curr_height)

print("스크롤 완료")
browser.get_screenshot_as_file("google_books.png") # 스크린샷 저장

import requests
from bs4 import  BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')

# jscontroller="jZ2Ncd"
books = soup.find_all("div", attrs={"class": "VfPpkd-EScbFb-JIbuQc UVEnyf"})

print(len(books))
for book in books:
    # print(f'book: {book}')
    title = book.find("div", attrs={"class": "Epkrse"}).get_text()
    org_price = book.find("span", attrs={"class": "SUZt4c P8AFK"})
    if org_price:
        org_price = org_price.get_text()
    else:
        org_price = "NOT ON SALE"
    price = book.find("span", attrs={"class": "VfPpfd VixbEe"}).get_text()
    link_url = book.find("a", attrs={"class": "Si6A0c ZD8Cqc"})["href"]

    # print(f"Title: {title} | Price: {price} | Original Price: {org_price} | Link: {"https://play.google.com"+link_url}")
    print(f"제목: {title}")
    print(f"금액: {price}")
    print(f"활인전금액: {org_price}")
    print(f"링크: {"https://play.google.com"+link_url}")
    print("-" * 100)

browser.quit()