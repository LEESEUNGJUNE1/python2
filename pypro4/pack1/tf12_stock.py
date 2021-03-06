# 다중선형회귀 : 주식 데이터로 회귀모델 작성. 하루 전 데이터로 다음날 종가 예측
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

xy = np.loadtxt("../testdata/stockdaily.csv", delimiter = ",", skiprows = 1)
print(xy[:2], len(xy))

scaler = MinMaxScaler(feature_range=(0,1))  # 정규화
xy = scaler.fit_transform(xy)
print(xy[:2], len(xy))

x_data = xy[:, 0:-1]    # Open,High,Low,Volume : feature
y_data = xy[:, [-1]]    # Close : label
print(x_data[:2])
print(y_data[:2])
print()
print(x_data[0], y_data[0])
print(x_data[1], y_data[1])
print()
x_data = np.delete(x_data, -1, 0)
y_data = np.delete(y_data, 0)
print(x_data[0], y_data[0])

print('---')
model = Sequential()
model.add(Dense(units=1, input_dim=4, activation='linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model.fit(x_data, y_data, epochs=100, verbose=0)
print('evaluate : ', model.evaluate(x_data, y_data))

print(x_data[10])
test = x_data[10].reshape(-1,4)
print('실제값 : ', y_data[10])
print('예측값 : ', model.predict(test).flatten())  # flatten() 2->1 차원으로 변경
print()
pred = model.predict(x_data)
from sklearn.metrics import r2_score
print('r2_score : ', r2_score(y_data, pred))

#plt.plot(y_data, 'b')
#plt.plot(pred, 'r--')
#plt.show()

print("--- \n과적합 방지를 목적으로 train / test로 분리 ---")
from sklearn.model_selection import train_test_split
#a,b,c,d = train_test_split(x_data, y_data, shuffle = False)
# 시계열 데이터[(자연어) 순서가있는데이터]는 섞이면 안되서 shuffle = False를 준다.
train_size = int(len(x_data) * 0.7)
test_size = len(x_data) - train_size
print(train_size, test_size) # 511 220
x_train, x_test = x_data[0:train_size], x_data[train_size:len(x_data)]
print(x_data[:2])
print(x_train[:2], x_train.shape, ' ', x_test[:2], x_test.shape)
print()
y_train, y_test = y_data[0:train_size], y_data[train_size:len(x_data)]
print(y_train[:2], y_train.shape, ' ', y_test[:2], y_test.shape)

print('~~~~~~~~~~~~~~~~~~~~~~')
model2 = Sequential()
model2.add(Dense(units=1, input_dim=4, activation='linear'))

model2.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model2.fit(x_train, y_train, epochs=100, verbose=0) # 학습은 train
print('evaluate2 : ', model2.evaluate(x_test, y_test))

print(x_test[10])
test = x_test[10].reshape(-1,4)
print('실제값2 : ', y_test[10])
print('예측값2 : ', model2.predict(test).flatten())  # flatten() 2->1 차원으로 변경
print()
pred2 = model2.predict(x_test)
print('split after - r2_score : ', r2_score(y_test, pred2))

print('~~~ keras를 이용해보자 ~~~')
# fit(학습) 도중에 검증도 함께 하고자 할 경우, train data를 다시 분리해 validation data를 운영할 수 있다.
# 과적합 방지 목적
model3 = Sequential()
model3.add(Dense(units=1, input_dim=4, activation='linear'))

model3.compile(optimizer='sgd', loss='mse', metrics=['mse'])
model3.fit(x_train, y_train, epochs=100, validation_split=0.15, verbose=0) # 학습은 train
print('evaluate3 : ', model3.evaluate(x_test, y_test))
pred3 = model3.predict(x_test)
print('split validation after - r2_score : ', r2_score(y_test, pred3))

plt.plot(y_data, 'b')
plt.plot(pred3, 'r--')
plt.show()



# 모델의 최적화를 위한 작업들이다.
# 그후 저장하고 팀원들에게 분배