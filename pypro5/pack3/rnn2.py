# 문자열 토큰 처리 + LSTM 으로 감성분류 
from keras.preprocessing.text import Tokenizer

samples = ['The cat say on the mat.','The dog ate my homework.']

# 토큰 분리 방법 1
token_index = {}

for sam in samples:
    for word in sam.split(sep=' '):
        if word not in token_index:
            #print(word)
            token_index[word] = len(token_index)
print(token_index)
            
print()
# 토큰 분리 방법 2 : Tokenizer
tokenizer = Tokenizer(num_words=15)
tokenizer.fit_on_texts(samples) # token 처리
token_seq = tokenizer.texts_to_sequences(samples)
print(token_seq)    # [[1, 2, 3, 4, 1, 5], [1, 6, 7, 8, 9]] 
print(tokenizer.word_index)     # {'the': 1, 'cat': 2, 'say': 3, 'on': 4, 'mat': 5, "'": 6, "'the": 7, 'dog': 8, 'ate': 9, 'my': 10, 'homework': 11}

print('--------')
token_met = tokenizer.texts_to_matrix(samples, mode = 'binary')  # 'count', 'tfidf','freq','binary'
print(token_met)

print(tokenizer.word_counts)
print(tokenizer.document_count)
print(tokenizer.word_docs)

print()
from keras.utils import to_categorical
print(to_categorical(token_seq[0], num_classes=6))

print('------')
docs = ['너무 재밌어요','최고예요','참 잘 만든 작품이에요','추천하고 싶어요','한번 더 보고 싶어요',
        '글쎄요','별로인데요','생각보다 만족스럽지 않네요','마음에 들지 않아요','재미없어요']

import numpy as np
labels = np.array([1,1,1,1,1,0,0,0,0,0])    # 1: 긍정, 0: 부

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)

x = token.texts_to_sequences(docs)
print('토큰화 결과 :',x)


print()
# 토큰 인덱싱 벡터의 크기를 일정하게 만들기 
from keras.utils import pad_sequences
padding_x = pad_sequences(x,4)
print('패딩 결과:', padding_x)

word_size = len(token.word_index) + 1 # 임베딩에 입력될 단어의 수. 가능한 토큰의 수는 단어 인덱스 최대값 + 1
print(word_size)    # 21

# model
from keras.models import Sequential
from keras.layers import SimpleRNN, LSTM, GRU, Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(word_size, 8, input_length=4))
model.add(LSTM(32, activation='tanh'))  # activation= 설정하지 X 'tanh' 이 기본값
model.add(Flatten())    # FClayer
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padding_x, labels, epochs=30, verbose=2)
print('acc score : %.4f'%(model.evaluate(padding_x, labels)[1]))

print('예측값 : ', np.where(model.predict(padding_x) > 0.5,1,0).ravel())
print('실제값 : ', labels)

