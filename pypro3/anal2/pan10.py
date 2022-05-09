# 네이버 제공 영화 랭킹 읽기 

from bs4 import BeautifulSoup

# 방법1 : urllib.request
import urllib.request
from anaconda_navigator.utils.py3compat import request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
data = urllib.request.urlopen(url)

soup = BeautifulSoup(data, 'lxml')

#print(soup.select("div.tit3"))
#print(soup.select("div[class=tit3]"))
#print(soup.find_all("div",{'class':'tit3'}))
print(soup.findAll("div",{'class':'tit3'}))

for tag in soup.findAll("div",{'class':'tit3'}):
    print(tag.text.strip())         # 공백 자르고 읽어오기 
    
print('-----'*10)
# 방법2 : requests
import requests
data = requests.get(url).text
soup2 = BeautifulSoup(data,'lxml')
m_list = soup.find_all('div','tit3')

#print(m_list)   
count = 1                   # title 순위 정하기
for i in m_list:
    title = i.find('a')
    print(str(count)+"위:" + title.string)
    count += 1

    