# https://velog.io/@dlskawns/Linear-Regression-%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EC%9D%98-%ED%8F%89%EA%B0%80-%EC%A7%80%ED%91%9C-MAE-MSE-RMSE-R-Squared-%EC%A0%95%EB%A6%AC
# Linear Regression - 선형회귀의 평가 지표, MAE, MSE, RMSE, R Squared 정리
# MAE(Mean Absolute of Errors) 평균절대오차
# 평균절대오차는 예측값 - 관측값들의 제곱이 아닌 절대값을 통해 음수를 처리한 뒤, 이들의 평균을 통해 구할 수 있다. 제곱을 하지 않기 때문에 단위 자체가 기존 데이터와 같아 회귀계수 증감에 따른 오차를 쉽게 파악할 수 있다.

# MSE(Mean Square of Errors) 평균제곱오차
# 평균제곱오차는 잔차제곱합(RSS)을 해당 데이터의 개수로 나누어서 구할 수 있다. 예측값 - 관측값(데이터값)의 제곱된 값의 평균을 구하는 것이다. 여기서 잔차의 제곱을 하는 이유는 잔차의 값이 음수가 될 수 있는 것을 방지할 수 있고, 제곱을 함으로써 오차의 민감도를 높이기 위함이다.

# RMSE(Root Mean Square of Errors) 평균제곱오차제곱근
# 평균제곱오차MSE에 루트를 씌워주어 비교에 좋도록 한 평가지표이다.

# R2(R Squared Score) 결정계수
# 결정계수는 실제 관측값의 분산대비 예측값의 분산을 계산하여 데이터 예측의 정확도 성능을 측정하는 지표이다. 0~1까지 수로 나타내어지며 1에 가까울수록 100%의 설명력을 가진 모델이라고 평가를 하게된다.


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 공부시간에 따른 점수 표
df = pd.DataFrame({'Study time':[3,4,5,8,10,5,8,6,3,6,10,9,7,0,1,2],
           'Score':[76,74,74,89,92,75,84,82,73,81,89,88,83,40,70,69]})
print(df.head(3))

# 데이터셋 분리 (train / test 로 분리)
train, test = train_test_split(df, test_size = 0.4, random_state = 2)
X_train = train[['Study time']]     # matirx  왜냐하면 sklearn의 LinearRegression을 사용하기 때문
y_train = train['Score']            # vector
X_test = test[['Study time']]
y_test = test['Score']
print(X_train)
print(y_train)
print(X_train.shape, X_test.shape, ' ',y_train.shape, y_test.shape) # (9, 1) (7, 1)   (9,) (7,)

# LinearRegression 진행
model = LinearRegression()
model.fit(X_train, y_train)     # 모델학습은 train data를 사용
y_pred = model.predict(X_test)
print('예측값:', y_pred)   # [81.82733051 92.47669492 ....

# 결정계수 수식으로 직접 구하기 (모델 성능 파악용 : test data를 사용)
# 잔차 구하기
y_mean = np.mean(y_test) # y 평균값

# $\sum(y 예측값 - y 평균값)^2$ = 예측값에 대한 편차
nomerator = np.sum(np.square(y_test - y_pred)) 

# $sum(y 관측값 - y 평균값)^2$
denominator = np.sum(np.square(y_test - y_mean))
r2 = 1 - nomerator / denominator    # 1 - (오차제곱합 / 편차제곱합) 
print('결정계수:', r2)  # 결정계수: 0.66321792

# r-square 함수사용
from sklearn.metrics import r2_score
print('결정계수:', r2_score(y_test, y_pred))    # test data를 사용

#R2값은 위에서 언급한 바와 같이 분산을 기반으로 측정하는 도구이므로 중심극한정리에 의해서 표본 데이터가 많을수록 그 정확도 역시도 올라가게된다. 
#PLOT을 이용해서 보면 그 예측 정확도가 달라지는걸 알 수 있다.

import seaborn as sns
import matplotlib.pyplot as plt

# 함수 작성
def linearregression(df, test_size):
    train, test = train_test_split(df, train_size = test_size, random_state = 2)
    X_train = train[['Study time']]
    y_train = train['Score']
    X_test = test[['Study time']]
    y_test = test['Score']

    # LinearRegression 진행
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # R2 계산
    print('R제곱 값:', r2_score(y_test, y_pred).round(2))
    print('Train data 비율: 전체 데이터 수의 {0}%'.format(i*100))
    print('Train data 수: {0}개'.format(len(X_train)))
    # 플롯 그리기
    sns.scatterplot(x = df['Study time'], y = df['Score'], color = 'green')
    sns.scatterplot(x = X_test['Study time'], y = y_test, color = 'red');
    sns.lineplot(x = X_test['Study time'], y = y_pred, color = 'red');
    plt.show()

test_sizes = [0.1,0.2,0.3,0.4,0.5]
for i in test_sizes:
    linearregression(df, i)
# 이미지와 같이 train data 수가 작을때는 오차가 너무 커서 음수가 나오다가도 데이터가 어느정도 이상이 되면 괜찮은 R제곱 값을 찾아가는 것을 확인 할 수 있다.