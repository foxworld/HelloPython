import requests
from bs4 import BeautifulSoup

#url = "https://comic.naver.com/webtoon"
url = "https://www.ksnet.co.kr/Kspay/Intro"
res = requests.get(url)
res.raise_for_status()
# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a)  # soup 객체에서 처음 발견된 a element 출력
print(soup.a.attrs)  # meta 속성 정보 출력
print(soup.a['href'])  #  속성 정보중 name 의 값 정보 출력
print("-" * 100)

print(soup.find("a", attrs={"class": "goBody"}))  # element 중 속성정보에 해당하는것만 출력
print(soup.find(attrs={"class": "goBody"}))
print("-" * 100)

rank1 = soup.find("li", attrs={"class": "on"})
print(rank1)
print("-" * 100)
print(rank1.a.get_text().strip())
rank2 = rank1.next_sibling.next_sibling
print(rank2.a.get_text().strip())
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text().strip())
print("-" * 100)
print(rank3.previous_sibling.previous_sibling.a.get_text())
print("-" * 100)
print(rank1.parent)
print("-" * 100)

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())
print("-" * 100)

print(rank1.find_next_siblings("li"))
print("-" * 100)

webtoon = soup.find("a", string="결제데모")
print(webtoon)
