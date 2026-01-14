import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=mkdocvzm&channel=user&page=1"

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# print("status :", res.status_code)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_selector("img")
    html = page.content()
    # print(html[:1000])
    browser.close()
soup = BeautifulSoup(html, "lxml")
# print(soup)

# items = soup.find_all("li", attrs={"class":re.compile("ProductUnit_productUnit__Qd6sv")})
items = soup.find_all("li", attrs={"class":re.compile("ProductUnit_productUnit*")})
print(items)
for item in items:
    print(item.find("div", attrs={"class":re.compile("ProductUnit_productNameV2*")}))
    print(item.find("div", attrs={"class":re.compile("ProductUnit_productNameV2*")}).get_text(strip=True))
