# bmi(체중) dataset으로 분류
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
import tensorflow as tf

bmi = pd.read_csv("bmi.csv")
print(bmi.head(2), bmi.shape)   # (50000, 3)
# 정규화
bmi['height']/= 200
bmi['weight']/= 100
print(bmi.head(2), bmi.shape)
# 매트릭스
x = bmi[['height','weight']].values
print(x[:2])

# label은 one-hot Encoding처리
bclass = {'thin':[1,0,0],'normal':[0,1,0],'fat':[0,0,1]}
y = np.empty((50000, 3))
print(y[:2])

for i, v in enumerate(bmi['label']):
    y[i] = bclass[v]
print(y[:2])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

print()
# model
model = Sequential()
model.add(Dense(128, input_shape=(2,), activation='relu'))
model.add(Dropout(0.2)) # 20%는 학습에서 제외하라 랜덤하게
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))   # 분류가 3개이상이니까 softmax를 사용

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

print(model.summary())

from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='loss', mode='auto', baseline=0.05, patience=5)

model.fit(x_train, y_train, batch_size = 64, epochs=10000, validation_split=0.2,
          verbose=2, callbacks=[es])

# evaluate
m_score = model.evaluate(x_test, y_test)
print('loss : ', m_score[0])
print('accuracy : ', m_score[1])

# predeict
print('예측값 : ', np.argmax(model.predict(x_test[:1]), axis = 1))
print('실제값 : ', np.argmax(y_test[:1]))

# new data
print('예측값 : ', np.argmax(model.predict(np.array([[187/200, 55/100]])), axis = 1))
print('실제값 : ', np.argmax(model.predict(np.array([[157/200, 75/100]])), axis = 1))

