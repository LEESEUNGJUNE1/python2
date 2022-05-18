# 노드를 증가 시키는 방법
# 학습진행과정을 시각화 시키는 방법
# units, epochs 가 중요하다.

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

# OR 게이트 논리 모델을 생성 후 처리
# 1. 데이터 셋 생성
x = np.array([[0,0],[0,1],[1,0],[1,1]]) # 매트릭스
y = np.array([0,1,1,1]) # 백터

print(x)    # feature
print(y)    # label(class)
#    모델 구성 방법1
#model = Sequential([
#    Dense(input_dim = 2, units=1),
#    Activation('sigmoid')
#])
#    모델 구성 방법2
#model = Sequential()
#model.add(Dense(units=5, input_dim = 2)) # (5개로 내보내줘, 2개를 입력받아)
#model.add(Activation('relu'))
#model.add(Dense(units=1))   # (1개로 내보내줘)
#model.add(Activation('sigmoid'))
#    모델 구성 방법3
model = Sequential()
model.add(Dense(units=5, input_dim = 2, activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=1, activation='sigmoid')) # sigmoid: 0,1 로만 값을 내보내준다. (=2항분류에서 사용)

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['acc'])

history = model.fit(x, y, epochs=100, batch_size=1, verbose=0)  # batch_size
loss_metrics = model.evaluate(x, y)
print('loss_metrics : ',loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
#print('예측결과 : ', pred)
print('예측결과 : ', pred.flatten())

print('history : ',history.history)
print('loss : ',history.history['loss'])
print('acc : ',history.history['acc'])

# 학습 진행 중 loss, acc 를 시각화
#import matplotlib.pyplot as plt
#plt.plot(history.history['loss'], label='train loss')
#plt.plot(history.history['acc'], label='train acc')
#plt.xlabel('epochs')
#plt.legend(loc='best')
#plt.show()

print('--- 모델의 구조 살펴보기 ---')
print(model.layers)
print(model.summary()) # 모델의 데이터와 레이어를 확인할수가 있다.

print('--- 가중치와 다중치 ---')
print(model.weights)    # summary를 더 많이 활용한다.