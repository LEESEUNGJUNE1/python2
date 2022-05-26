# 네이버의 영화 정보 사용
# 5편의 영화 리뷰를 읽어 형태소 분석 후 CountVectorizer, TfidfVectorizer 적용
# 각 영화 간의 유사도(COS유사도) 확인
# 웹사이트의 글자를 긁어와서 그 페이지에 연관된 글자들에 관하여 정리해보는
import requests
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# 웹사이트에서 데이터 긁어오기 
def movie_scrap_func(url):
    result = []
    for p in range(1, 6):
        r = requests.get(url + "&page=" + str(p))
        # print(r)    #<Response [200]>
        soup = BeautifulSoup(r.content, 'lxml', from_encoding='ms949')
        # print(soup)
        title = soup.find_all("td", {"class":"title"})
        # print(title[1].text)
        sub_result = []
        for i in range(len(title)):
            sub_result.append(title[i].text # 지우고싶은 단어들 선택중
                              .replace("\r","")
                              .replace("\n","")
                              .replace("\t","")
                              .replace("신고","")
                              .replace("별점","")
                              .replace("총","")
                              .replace("점","")
                              .replace("중","")
                              .replace("범죄도시2","")
                              .replace("범죄도시","")
                              .replace("ㅋ","")
                              .replace("ㅠ","")
                              .replace("영화","")
                              )
            result = result + sub_result
        return("".join(result))
    
city2 = movie_scrap_func('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=192608&target=after')
doctor = movie_scrap_func('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=182016&target=after')
knife = movie_scrap_func('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=196051&target=after')
romans = movie_scrap_func('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=196809&target=after')
hunt = movie_scrap_func('https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=174808&target=after')
movies = [city2,doctor,knife,romans,hunt]
print(movies)

print(' - 형태소 분석을 할꺼야 : 명사,형용사를 취할꺼야 - ')
okt = Okt()

def word_separate(movies):
    result=[]
    for movie in movies:
        words = okt.pos(movie)
        one_result = []
        for word in words:
            if word[1] in ['None', 'Adjective'] and len(word[0]) >=2:   # 2글자 이상만
                one_result.append(word[0])
        result.append(" ".join(one_result))
    return result

word_list = word_separate(movies)
print(word_list)

print(' --- CountVectorizer, TfidfVectorizer 를 사용해보자 ---')
# CountVectorizer
count = CountVectorizer(min_df = 2) # 문서집합으로 단어 수를 세어 BOW 벡터를 만듦 (빈도수가 2 미만은 무시하겠어)
count_dtm = count.fit_transform(word_list).toarray()
print(count_dtm)
print(' ---    ---- ')
# count_dtm을 DataFrame에 저장해볼게
cou_dtm_df = pd.DataFrame(count_dtm,
                          columns=count.get_feature_names(),
                          index = ['city2','doctor','knife','romans','hunt'])
print(cou_dtm_df)


# TfidfVectorizer : 단어의 빈도수에 추가적으로 단어의 중요성까지 가중치로 표현
idf_maker = TfidfVectorizer(min_df=2)
tfidf_dtm = idf_maker.fit_transform(word_list).toarray()
print(tfidf_dtm)

tfidf_dtm_df = pd.DataFrame(tfidf_dtm,
                          columns=idf_maker.get_feature_names(),
                          index = ['city2','doctor','knife','romans','hunt'])
print(tfidf_dtm_df)

print('~~~ 각 영화 간에 유사도 확인 : COS 유사도 공식 사용 ~~~')
def cosine_function(doc1, doc2):
    bunja = sum(doc1 * doc2)
    bunmo = (sum(doc1 ** 2) * sum(doc2 ** 2)) ** 0.5
    return bunja / bunmo

res = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        res[i, j] = cosine_function(tfidf_dtm_df.iloc[i], tfidf_dtm_df.iloc[j].values)
        
# print(res)

df = pd.DataFrame(res, index = ['city2','doctor','knife','romans','hunt'],
                  columns = ['city2','doctor','knife','romans','hunt'])
print(df)
