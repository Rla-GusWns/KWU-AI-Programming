#pip install webdriver_manager chrome manager 관리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

f= open('wordcloud.txt','w',encoding='UTF-8')

#시스템에 부착된 장치가 작동하지 않습니다 오류 제거
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8")
kbo = driver.find_elements(by=By.XPATH,value="//div[text()]") # text 속성을 가진 요소들을 다 크롤링

for k in kbo:
    f.write(k.text) #문서화 시키기 위해서 txt 파일에 저장중
    
driver.close()

f.close()

text =''

f1= open('wordcloud.txt','r',encoding='UTF-8') #아까 만든 문서를 토대로 wordcloud를 생성하기 위해 읽기모드로 불러온다 
lines = f1.readlines()

for line in lines:
    text +=line
    
f1.close()

s_words = STOPWORDS.union({'있다','없다','수','펼치기','접기','자세한','내용은','외부','광고로','때문에','은','는','이','가','예를','들어','문서','참조'})

wc = WordCloud(font_path='C:/WINDOWS/FONTS/MALGUNSL.TTF',background_color="white",width=1000,height=700,stopwords=s_words).generate(text)
plt.figure(figsize =(40,30))
plt.imshow(wc)
plt.show()