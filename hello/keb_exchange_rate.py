import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime

import jaydebeapi

def db_connect():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 프로젝트 루트(한 단계 위)
        base_dir = os.path.abspath(os.path.join(current_dir, ".."))
        # print("base_dir:", base_dir)

        h2_driver_path = f"{base_dir}/libs/h2-2.3.232.jar"
        driver_class = "org.h2.Driver"
        database_url = "jdbc:h2:tcp://localhost/~/test"
        user_info = ["sa", ""]
        conn = jaydebeapi.connect(driver_class, database_url, user_info, h2_driver_path)
        print("conn:", conn)
        return conn
    except Exception as e:
        print("DB 연결 실패:", e)
        return None

def db_disconnect(conn):
    conn.close()
    print("Database connection closed.")

def convert_date(date_str: str) -> str:
    # "YYYYMMDD" → "YYYY-MM-DD"
    dt = datetime.strptime(date_str, "%Y%m%d")
    return dt.strftime("%Y-%m-%d")

def insert_first_exchange_rate(data):
    conn = db_connect()
    if conn is None:
        return

    cursor = conn.cursor()
    # delete
    print("### delete data for date:", data[0])
    sql = "DELETE FROM PGUSD01 where tr_date = ?;"
    cursor.execute(sql, (data[0],))

    # insert
    print("### insert data:", data)
    sql = "INSERT INTO PGUSD01 (tr_date, usd_rate) values (?, ?);"
    cursor.execute(sql, data)
    conn.commit()

    # select
    print("### select data for date:", data[0])
    sql = "SELECT * FROM PGUSD01 where tr_date = ?;"
    cursor.execute(sql, (data[0],))
    rows = cursor.fetchall()
    for row in rows:
        print(f"tr_date: {row[0]}, usd_rate: {row[1]}")

    db_disconnect(conn)

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
    print("url:", url)
    soup = create_soup(url)
    # print(soup.prettify())

    with open("files/exchange.html", "w", encoding="utf8") as f:
        f.write(soup.prettify())

    base_date = soup.select_one("p.txtRateBox").find("strong").get_text(strip=True)
    replace_word = base_date.replace("년", "").replace("월", "").replace("일", "").strip()
    print(f"조회일자: {target_date} 기준일자: {base_date}({replace_word})")

    if target_date != replace_word:
        print("해당 일자의 환율 정보가 없습니다.")
        return

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

        fx_check_data = [target_date, data['외화수표 파실 때'].replace(',','')]
        insert_first_exchange_rate(fx_check_data)

if __name__ == "__main__":
    # get_exchange_rate("20260203")

    today = datetime.today().strftime('%Y%m%d')
    get_exchange_rate(today)

