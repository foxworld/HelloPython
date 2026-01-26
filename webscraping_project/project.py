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

    weather = soup.find("div", attrs={"class":"status_wrap"})
    # today_weather_temperature = weather.find("div", attrs={"class":"temperature_text"} ).get_text()
    # today_weather_expressions = weather.find("span", attrs={"class":"weather before_slash"} ).get_text()
    # summary = weather.find("p", attrs={"class":"summary"} )
    # temperature_up = weather.find("span", attrs={"class":"temperature up"} )
    # blind = weather.find("span", attrs={"class":"blind"})
    #
    # print(weather)
    # print(today_weather_temperature.strip())
    # print(today_weather_expressions)
    # print(summary)
    # print(blind)

    summary = weather.select_one("p.summary").get_text(strip=True)
    # 온도 전체 (1.1° 높아요)
    temperature_full = weather.select_one("span.temperature").get_text(strip=True)
    # 온도 숫자만 (1.1°)
    temperature_only = weather.select_one("span.temperature").contents[0].strip()
    # 날씨 (맑음)
    weather = weather.select_one("span.weather").get_text(strip=True)
    print("summary:", summary)
    print("temperature_full:", temperature_full)
    print("temperature_only:", temperature_only)
    print("weather:", weather)




if __name__ == "__main__":
    get_weather() # 오늘 날씨정보 가져오기
