print('---일정 시간 마다 웹 문서 스크래핑----------------------------')
import datetime
import time
import urllib.request as req
from bs4 import BeautifulSoup

def working_func():
    url ="https://finance.naver.com/marketindex/"
    data = req.urlopen(url)
    
    soup = BeautifulSoup(data,'lxml')
    price = soup.select_one("div.head_info > span.value").string
    print('미국 USD : ', price)
    t = datetime.datetime.now()     # 현재 시간 찍기
    print(t)
    fname = "./usd/" + t.strftime("%Y-%m-%d-%H-%M-%S") + '.txt'
    print(fname)
    with open(fname,mode = 'w') as f:
        f.write(price)

while True:
    working_func()
    time.sleep(3)   # 3초에 한번씩 

