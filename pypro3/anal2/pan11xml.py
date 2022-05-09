# BeautifulSoup으로 XML 문서 처리 
from bs4 import BeautifulSoup
import pandas as pd

with open('../testdata/my.xml', mode='r', encoding='UTF-8') as f:
    xmlfile = f.read()

print(xmlfile, type(xmlfile))  #  <class 'str'>

soup = BeautifulSoup(xmlfile, 'lxml')
print(soup, type(soup))        # <class 'bs4.BeautifulSoup'>

# print(soup.prettify())        
itemTag = soup.findAll('item')
print(itemTag[0])
print('-----'*10)

nameTag = soup.findAll('name')
print(nameTag[0]['id'])
print('-----'*10)
for i in nameTag:
    print(i['id'])

print('-----'*10)
for i in itemTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print('id:' + j['id'] + ', name:' + j.string)
    tel = i.find('tel')  
    print('tel:' + tel.string)
    for j in i.find_all('exam'):
        print('kor:' + j['kor'] + ', eng:' + j['eng'])
        
print('---기상청 제공 날씨 정보 읽기 -------------------')        
try:
    import urllib.request as req 
    url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
    plainText = req.urlopen(url).read().decode('UTF-8')
    #print(plainText)
    
    soup = BeautifulSoup(plainText, 'lxml')
    #print(soup)
    title = soup.find('title').string
    print(title)        # title 읽기 / 기상청 육상 중기예보
    
    # wf = soup.find('wf')
    # print(wf)
    city = soup.find_all('city')
    #print(city)
    cityDatas = []
    for c in city:
        cityDatas.append(c.string)
    df = pd.DataFrame()
    df['city'] = cityDatas
    #print(df)
    tempMins = soup.select("Location > province + city + data > tmn")   # +(형제 아래방향), -(형제 위방향)
    #print(tempMins)
    tempDatas = []
    for t in tempMins:
        tempDatas.append(t.string)
    df['temp_min'] = tempDatas
    df.columns = ['지역','최저기온']
    print(df.head(2))
    print(df.tail(2))
    
    # df를 file로 저장
    df.to_csv("날씨.csv", index = False)
    #print(pd.read_csv("날씨.csv"))
    
    print('-----'*10)       # 슬라이싱으로 나누기
    print(df[0:2])          # 앞 에서 2개
    print(df[-2:len(df)])   # 뒤 에서 2개
    
    print('-----'*10)
    print(df.iloc[0], type(df.iloc[0]))     # Series
    
    print('-----'*10)
    print(df.iloc[0:2,:])
    print(df.iloc[0:2, 0:1])
    print(df.iloc[0:2, 0:2])
    
    print('-----'*10)
    print(df.loc[1:3])
    print(df.loc[[1,3]])
    
    print('-----'*10)
    print(df.loc[1:3,['최저기온','지역']])
    
    print('-----'*10)
    print(df['최저기온'].mean())
    print(df['최저기온'].describe())
    
    print('-----'*10)
    df = df.astype({'최저기온':int})    # 문자를 int 를 형 변환
    print(df.loc[df['최저기온'] >= 10])
    print(df.loc[(df['최저기온'] >= 10) & (df['최저기온'] >=12)])
    
    print('-----'*10)
    print(df.sort_values(['최저기온'], ascending = True))
    
    
    
    
except Exception as e:
    print('err : ', e)
