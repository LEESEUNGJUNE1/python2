# 자연어 처리
# word embedding : 워드를 수치화 해서 벡터화
# 카데고리컬 인코딩 : 레이블 인코딩(문자->숫자), 원핫 인코딩(0,1 로 데이터를 변환) 등등..

print('label encoding을 해보자 !')
datas = ['python', 'len',' program','computer','say']
datas.sort()
print(datas)
# 인덱싱 하기
values=[]
for x in range(len(datas)):
    values.append(x)

print(values, '', type(values))

print('One-Hot Encoding 을 해보자..')
import numpy as np
onehot = np.eye(len(datas))
print(onehot, '', type(onehot))

print('label encoding : Class를 사용해보자...')
from sklearn.preprocessing import LabelEncoder
datas = ['python', 'len',' program','computer','say']
encoder = LabelEncoder().fit(datas)
values = encoder.transform(datas)
print(values, '', type(values), np.sort(values))
print(encoder.classes_)

print('One-Hot Encoding : Class를 사용해보자....')
from sklearn.preprocessing import OneHotEncoder
labels = values.reshape(-1, 1)
print(labels, '', labels.shape)
onehot = OneHotEncoder().fit(labels)
onehotValues = onehot.transform(labels)
print(onehotValues.toarray())

# 밀집 표현 : 단어마다 고유한 일련번호를 메겨서 사용하는것이 아니라(label,onehot), 유사한 단어들을 비슷한 방향과 힘의 벡터를 갖도록 변환해 사용
# word2vec : 단어의 이미를 다차원 공간에 실수로 벡터화하는 분산표현 기법. 단어 간 유사성을 표현 가능
from gensim.models import word2vec
sentence = [['python', 'lan',' program','computer','say']]  # 중첩리스트를 써보겠다 [[]]
model = word2vec.Word2Vec(sentence, min_count=1, vector_size=30) # size or vectort_size
print(model)
word_vectors = model.wv
print('word_vectors : ', word_vectors)
print('word_vectors index : , ', word_vectors.key_to_index)
print('word_vectors index : , ', word_vectors.key_to_index.keys())
print('word_vectors index : , ', word_vectors.key_to_index.values())
vocabs = word_vectors.key_to_index.keys()
word_vectors_list = [word_vectors[v] for v in vocabs]
print(word_vectors_list[0], len(word_vectors_list[0]))
print(word_vectors_list[1], len(word_vectors_list[1]))

print(' --- 단어간의 유사도를 알아보자 --- ')
# 단어 간 유사도 (COS 유사도) 확인 : 두 벡터가 닮은 정도를 정량적(-1 ~ 0 ~ 1)으로 나타낼수있다.
print(word_vectors.similarity(w1='python', w2='lan'))
print(word_vectors.similarity(w1='python', w2='say'))
print(word_vectors.similarity(w1='lan', w2='computer'))

# 시각화
import matplotlib.pyplot as plt
def plot_func(vocabs, x, y):
    plt.figure(figsize=(8,6))
    plt.scatter(x,y)
    for i,v in enumerate(vocabs):
        plt.annotate(v, xy=(x[i],y[i]))
    
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
xys = pca.fit_transform(word_vectors_list)
xs = xys[:,0]
ys = xys[:,1]
plot_func(vocabs, xs, ys)
plt.show()


