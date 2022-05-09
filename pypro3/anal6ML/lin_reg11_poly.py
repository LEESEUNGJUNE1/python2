# 선형회귀 모델을 다항회귀로 변환
# 데이터가 선형가정이 어긋날 때 (정규성 불만족) 대처할 수 있는 방법으로 다항식 항을 추가한 다항회귀모델을 사용할 수 있다. 

import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([4,2,1,3,7])
# plt.scatter(x, y)
# plt.show()

# 선형회귀모델 작성
from sklearn.linear_model import LinearRegression
x = x[:, np.newaxis] # 차원 확대 ( vector -> matrix로 )
print(x)

model = LinearRegression().fit(x,y)
ypred = model.predict(x)
print(ypred)

plt.scatter(x, y)
plt.plot(x, ypred, c='red')
plt.show()

# 비선형 데이터인 경우에는 선형회귀모델로는 설명이 불완전함. 그래서 좀 더 복잡한 모델이 필요
# 모델에 유연성을 주기위해 입력 데이터에 특징 열을 추가
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=5, include_bias = False)   #  degree=열의 갯수
x2 = poly.fit_transform(x)      # 특징 행렬을 만든다.
print(x2)

model2 = LinearRegression().fit(x2, y)  # 특징 행렬값으로 학습
ypred2 = model2.predict(x2)
print(ypred2)

plt.scatter(x, y)
plt.plot(x, ypred2, c='blue')
plt.show()

# degree=값 이 얼마인가에 따라 다항식 모델의 성능이 달라진다.

