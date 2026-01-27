import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

for year in range(2018, 2020):
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            extra_http_headers={"Accept-Language": "ko-KR,ko;q=0.9",}
        )
        page = context.new_page()
        page.goto(url)
        page.wait_for_selector("img", timeout=60000)
        html = page.content()
        browser.close()

    soup = BeautifulSoup(html, "lxml")

    # divs = soup.find_all("div", attrs={"class":"item-thumb"})
    images = soup.find_all("img", attrs={"data-original-loaded":"true"})
    for idx, image in enumerate(images):
        if image:
            image_url = image['src']
            print(image_url)
            image_res = requests.get(image_url)
            image_res.raise_for_status()

            with open("files/movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
                f.write(image_res.content)

            if idx >=4: break
        else:
            continue

