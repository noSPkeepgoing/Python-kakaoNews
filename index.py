from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

# 크롬창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

# 카카오 뉴스창 접속하기
driver.get("https://www.kakaocorp.com/page/news/")

# 뉴스 정보를 담기 위한 리스트
titles = []
days = []
contants = []

# 제일 최근 뉴스 10개
for i in range(1, 11):
    news = driver.find_element(By.CSS_SELECTOR, '#tabNewsContent1 > li:nth-child({})'.format(i)).click()
    time.sleep(1)
    news_title = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/article/div[1]/h3').text
    news_day = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/article/div[1]/div[1]/span[2]').text
    news_contant = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/article/div[3]/div').text
    titles.append(news_title)
    days.append(news_day)
    contants.append(news_contant)
    driver.back()
    time.sleep(2)
driver.close()

# txt파일로 결과 출력
sys.stdout = open('result.txt', 'w')

for j in range(len(days)) :
    print('{} 일자 소식 : {}'.format(days[j] , titles[j]))
    print(contants[j])