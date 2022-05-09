# Linear Regression - 선형회귀의 평가 지표 score 정리 : MAE, MSE, RMSE, R_Squared

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler  # 데이터를 0 ~ 1 사이의 범위로 표준화

# 편차가 큰 표본 데이터 작성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 1, sample_size) + x * 30
print(x[:5])
print(y[:5])
print('상관계수 : ', np.corrcoef(x, y))  # 0.99939357

# 독립변수(x)에 대한 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))  # matrix 형태로 표준화
print(x_scaled[:5], x_scaled.shape)  # [[0.87492405] ...  (100, 1)

# 시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled, y)
# print(model.summary())    # 'LinearRegression' object has no attribute 'summary'

y_pred = model.predict(x_scaled)    # 학습한 데이터로 예측결과를 얻어 실제값과 비교
print('예측값 : ', y_pred[:5])     # [ 490.32381062 -182.64057041 -157.48540955 -321.44435455  261.91825779]
print('실제값 : ', y[:5])          # [ 482.83232345 -171.28184705 -154.41660926 -315.95480141  248.67317034]

print()
# 모델성능 파악
def regScore_func(y_true, y_pred):
    print('r2_score(결정계수):{}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(평균제곱근오차):{}'.format(mean_squared_error(y_true, y_pred)))
    # mean_squared_error : 잔차의 제곱의 합을 표본수로 나눈 값. 분산분석의 SSE와 같음
    
regScore_func(y_pred, y)
# r2_score(결정계수):0.9987860408174064
# explained_variance_score(설명분산점수):0.9987860408174064    # r2_score와 이 값이 다르면 에러에 편향이 있음. 모델 학습이 잘못 되었다는 뜻.
# mean_squared_error(평균제곱근오차):86.14795101998747

print('-------------'*10)
# 분산이 큰 표본 데이터 작성
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) + x * 30
print(x[:5])
print(y[:5])
print('상관계수 : ', np.corrcoef(x, y))  # 0.004011

# 독립변수(x)에 대한 표준화
scaler2 = MinMaxScaler()
x_scaled2 = scaler2.fit_transform(x.reshape(-1, 1))  # matrix 형태로 표준화
print(x_scaled2[:5], x_scaled2.shape)  # [0.45631435] (100, 1)

model2 = LinearRegression().fit(x_scaled2, y)
y_pred2 = model2.predict(x_scaled2)
regScore_func(y, y_pred2)
# r2_score(결정계수):1.6093526521765433e-05                         # 설명력이 매우 낮음
# explained_variance_score(설명분산점수):1.6093526521765433e-05
# mean_squared_error(평균제곱근오차):282457.9703485092                # 평균제곱근오차는 매우 커짐

