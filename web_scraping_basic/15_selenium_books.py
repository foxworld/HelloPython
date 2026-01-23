import requests
from bs4 import  BeautifulSoup

url = "https://play.google.com/store/books"
headers  ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

books = soup.find_all("div", attrs={"class": "VfPpkd-EScbFb-JIbuQc UVEnyf"})
print(len(books))
for book in books:
    # print(f'book: {book}')
    title = book.find("div", attrs={"class": "Epkrse"}).get_text()
    try:
        org_price = book.find("span", attrs={"class": "SUZt4c P8AFK"}).get_text()
    except AttributeError:
        org_price = "NOT ON SALE"
    price = book.find("span", attrs={"class": "VfPpfd VixbEe"}).get_text()

    print(f"Title: {title} | Price: {price} | Original Price: {org_price}")

with open("books.html", "w", encoding="utf8") as f:
    f.write(str(soup.prettify())) # html 문서 예쁘게 출력
