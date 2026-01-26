import requests
from bs4 import BeautifulSoup

# [오늘의 날씨]
# 흐림, 어제보다 00℃ 높아요
# 현재 00℃ (최저 00℃ / 최고 00℃)
# 강수확률 00
# 미세먼지 00㎕/㎥ 좋음
# 초미세먼지 00㎕/㎥ 좋음

def get_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&ackey=ue3ing4v"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    weather = soup.find("div", attrs={"class":"temperature_info"})
    print(weather)






if __name__ == "__main__":
    get_weather() # 오늘 날씨정보 가져오기
