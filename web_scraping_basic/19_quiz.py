import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EC%8B%9C%EC%84%B8&oquery=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=jUNhclqosAKssB12%2F2s-502728&ackey=dd0r19ba"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class": "list"}).find("tbody").find_all("tr", attrs={"class": "_land_tr_row"})
for index, row in enumerate(data_rows):
    columns = row.find_all("td")
    print(f"=========================== 매물 {index+1} ===========================")
    print(f"거래   : {columns[0].get_text(strip=True)}")
    print(f"소재지 : {columns[1].get_text(strip=True)}")
    print(f"단지명 : {columns[2].find("a").get_text()}")
    print(f"면적   : {columns[3].get_text()} (공급/전용)")
    print(f"매물가 : {columns[4].get_text()} 만원")
    print(f"층    : {columns[5].get_text()}")

