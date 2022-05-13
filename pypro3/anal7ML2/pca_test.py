# 주성분 분석(PCA) : 데이터 차원 축소 - 비슷한 열끼리 합치기 [비지도 학습]
# 원래 데이터 분사을 최대한 보존하는 새로운 축을 찾고, 그축에 데이터를 사영(projection) 시키는 방법(직교) 사용

# iris data를 사용해서 차원축소

from sklearn.decomposition import PCA
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data[:2])
n = 10
x = iris.data[:n, :2] # 0열과 1열만 가져와
print('차원 축소 전 : ', x, x.shape, type(x))
print(x.T)

"""
# 시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2),['꽃받침 길이', '꽃받침 폭'])
plt.xlabel('특성의 종류')
plt.ylabel('특성 값')
plt.title('붓꽃 크기 특성')
plt.legend(['표본 {}'.format(i + 1)for i in range(n)])
plt.grid
plt.show()
"""

"""
# x축에는 꽃받침의 길이, y 축에는 꽃받침의 폭 으로 산점도 출력
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker='s', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1], '표본{}'.format(i + 1))
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
"""
"""
# 두 개의 열의 값 패턴이 매우 유사함을 알 수 있다. 그러므로 차원축소 가능~ ==> PCA
pca1 = PCA(n_components = 1) # 변환 차원 수
x_low = pca1.fit_transform(x) # 비지도 학습으로 target은 지정하지 않음. 특정행렬을 낮은 차원의 근사행렬로 변환
print(x, '', x.shape) #(10, 2)
print('x_low', x_low, '', x_low.shape) # (10, 1)
# 차원 축소 값 원복
x2 = pca1.inverse_transform(x_low)
print('원복 값', x2, '', x2.shape) # (10, 2) 주성분 분석값 원복 결과 [5.1 3.5] ==> [[5.06676112 3.53108532]
print('원래 값', x[0, :])
print('주성분 값', x_low[0]) # 하나의 열로 모으는 과정
print('원복 값', x2[0, :])

# x축에는 꽃받침의 길이, y 축에는 꽃받침의 폭 으로 산점도 출력
df = pd.DataFrame(x)
ax = sns.scatterplot(df[0], df[1], data=df, marker='s', s=100, color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1], '표본{}'.format(i + 1))
    plt.plot([x[i, 0], x2[i, 0]], [x[i, 1], x2[i, 1]], 'k--') # 직교

plt.plot(x2[:, 0], x2[:, 1], 'o-', color='y', markersize = 10)
plt.plot(x[:, 0].mean() , x2[:, 1].mean(), 'D', color='r', markersize = 10)

plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('붓꽃 크기 특성(2차원)')
plt.axis('equal')
plt.show()
"""
# iris 4개의 열을 두 개로 축소
x = iris.data
print(x[:2])
pca2 = PCA(n_components = 2)
x_low2 = pca2.fit_transform(x) # 비지도학습이여서 x값만 주면 된다.
print('x_low2', x_low2, '', x_low2.shape)
print('근사행열 값 : ', pca2.explained_variance_ratio_) # 변동성 비율 제1 주성분, 제2 주성분
x_trans = pca2.inverse_transform(x_low2) # 원복값 구하는 식
print('원래 값', x[0, :])
print('주성분 값', x_low2[0]) # 근사행열로 변환했을때 원본값의 92.46% 설명함
print('원복 값 :', x_trans[0, :])

print()
iris1 = pd.DataFrame(x, columns=['sepal_length','sepal_width','petal_length','petal_width'])
print(iris1.head(5))
print('4개의 변수를 2개의 변수로 변환')
iris2 = pd.DataFrame(x_low2, columns=['var1','var2'])
print(iris2.head(5))

