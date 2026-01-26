from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
import time
interval = 2 # 2초에 한 번씩 스크롤 내리기

url = "https://play.google.com/store/books"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터 높이의 1080px 만큼 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 * 1080 해상도 기준
# browser.execute_script("window.scrollTo(0, 2080)") # 1920 * 1080 해상도 기준

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

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

import requests
from bs4 import  BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')

# jscontroller="jZ2Ncd"
books = soup.find_all("div", attrs={"class": "VfPpkd-EScbFb-JIbuQc UVEnyf"})
#books = soup.find_all("div", attrs={"jsdata":"QbiEs;YogBCj8KJAogcHJvbW90aW9uXzEwMDEwNjVfdG9wcGFpZF9ib29ra3IQAxIXChN0b3BfZGV2aWNlX2ZlYXR1cmVkEANKQAo-CBQQ3durygwQrNH_kw0Q86mDpQUQ_PzFlQQQ0-rEgg4Q-9ev1A8Qtar45QsQg5vg9QQQ8bLbxAkQ7JCSxAZQFPgBAA;$848"})

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

# with open("books.html", "w", encoding="utf8") as f:
#     f.write(str(soup.prettify())) # html 문서 예쁘게 출력

time.sleep(30)
browser.quit()