import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime

import jaydebeapi

def convert_date(date_str: str) -> str:
    # "YYYYMMDD" → "YYYY-MM-DD"
    dt = datetime.strptime(date_str, "%Y%m%d")
    return dt.strftime("%Y-%m-%d")

def insert_exchange_rate(data):
    h2_jar = "C:/IdeaProjects/study/HelloPython/libs/h2-2.3.232.jar"
    conn = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost/~/test",
        ["sa", ""],
        h2_jar
    )
    print(conn)

    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print(result)

    sql = "INSERT INTO PGUSD01 (tr_date, usd_rate) values (?, ?);"
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

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

def get_exchange_rate(target_date):
    # url = f"https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do?ajax=true&curCd=USD&tmpInqStrDt={convert_date(target_date)}&inqStrDt={target_date}&pbldDvCd=1&inqKindCd=1&requestTarget=searchContentDiv"
    url = f"https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do?curCd=USD&pbldDvCd=1&inqKindCd=1&inqStrDt={target_date}"
    soup = create_soup(url)
    # print(soup.prettify())

    with open("files/exchange.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

    rows = soup.select("tbody tr")  # 모든 환율 행
    for row in rows:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]

        if len(cols) < 11:
            continue  # 데이터가 부족한 행은 스킵

        data = {
            "통화": cols[0],
            "사실 때 환율": cols[1],
            "사실 때 스프레드": cols[2],
            "파실 때 환율": cols[3],
            "파실 때 스프레드": cols[4],
            "송금 보낼 때": cols[5],
            "송금 받을 때": cols[6],
            "외화수표 파실 때": cols[7],
            "매매 기준율": cols[8],
            "환가료율": cols[9],
            "미화 환산율": cols[10],
        }
        print(data)

        pgusd01_data = [target_date, data['외화수표 파실 때'].replace(',','')]
        # insert_exchange_rate((pgusd01_data))

if __name__ == "__main__":
    today = datetime.today().strftime('%Y%m%d')
    get_exchange_rate(today)
