# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. 네이버 이동
browser.get("https://naver.com")
# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

# 3. id / pw 입력
browser.find_element(By.ID, "id").send_keys("userid")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
# browser.find_element(By.ID, "log.login").click()

time.sleep(3)
# 5. 새로입력
browser.find_element(By.ID, "id").clear()
browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.print_page())

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 브라우저 종료


#elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
# elem.click()
# elem.back()
# elem.forward()
# elem.refresh()

# elem = browser.find_element(By.ID, "query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# elem = browser.find_elements(By.TAG_NAME, "a")
# for e in elem:
#     e.get_attribute("href")

# browser.get("https://daum.net")
# elem = browser.find_element(By.NAME, "q")
# elem.send_keys("나도코딩")
# elem = browser.find_element(By.XPATH, "//*[@id=\"daumSearch\"]/fieldset/div/div/button[3]")
# elem.click()
# browser.quit() # 브라우저 종료

