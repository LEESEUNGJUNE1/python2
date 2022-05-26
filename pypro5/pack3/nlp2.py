# 웹 뉴스 자료 읽어 형태소 분석 후 word2vec을 이용해 단어간 유사도 확인하기
import pandas as pd
from konlpy.tag import Okt

okt = Okt()

with open('news.txt', mode='r', encoding='utf-8') as f:
    lines = f.read().split('\n')

print(len(lines))

wordDic = {}    # 형태소 분석 후 명사만 추출해 단어별 빈도수 => {'자동차':5...

for line in lines:
    datas = okt.pos(line)
    # print(datas) # [('브랜드', 'Noun'), ('별로', 'Noun'), ...
    for word in datas:
        if word[1] == 'Noun':
            # print(word[0])  # 명사만 볼수있다.
            if not(word[0] in wordDic):
                wordDic[word[0]]=0

            wordDic[word[0]]+=1

print(wordDic)

keys = sorted(wordDic.items(), key = lambda x:x[1], reverse = True) # 많은순서대로 정렬해줘
print(keys)
print(' - 스무개만 데이터에 담아보자 - ')
wordList = []
countList = []

for word, count in keys[:20]:
    wordList.append(word)
    countList.append(word)

df = pd.DataFrame()
df['word'] = wordList
df['count'] = countList
print(df)
print(' ## 두 글자 이상의 데이터를 읽어 파일로 저장 ## ')
results = []

with open('news.txt', mode='r', encoding='utf-8') as f:
    lines = f.read().split('\n')
    for line in lines:
        datas = okt.pos(line, stem=True)    # 원형 어근 출력. ex)한가한->한가하다
        imsi = []
        # print(datas) <- 어떤데이터를 가져올지 확인하기위해
        for word in datas:
            if not word[1] in ['Number','Alpha','Foreign','Josa','Punctuation','Determiner','Modifier','None','Verb']:
                if len(word) >= 2:
                    imsi.append(word[0])
        # print(imsi)
        imsi2 = (" ".join(imsi).strip())
        results.append(imsi2)
print(results)

fileName = 'news2.txt'
with open(fileName, 'w', encoding='utf-8') as fw:
    fw.write('\n'.join(results))
print('저장 성공!')

print(' ~~~ word2vec으로 밀집백터를 만든 후 단어 유사도 확인 ~~~ ')
from gensim.models import word2vec

lineObj = word2vec.LineSentence(fileName)   # 파일을 읽었다.

model = word2vec.Word2Vec(sentences=lineObj, vector_size=100, min_count=1, sg=0, window = 10)
# sg=0 : CBOW - 주변단어로 중심단어 예측방식,
# sg=1 : Skip-gram - 중심단어로 주변단어 예측방식,

print(model)

print(model.wv.most_similar(positive=['전기차']))
print(model.wv.most_similar(positive=['전기차'], topn=3))  # topn=3 가까운 3개를 출력해
print(model.wv.most_similar(positive=['전기차','메르세데스'], topn=3))
print(model.wv.most_similar(negative=['메르세데스']))  # negative-관련이 없는 

