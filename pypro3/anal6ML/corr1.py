# 상관관계 분석
# 두 개 이상의 확뷸변수(연속형) 간에 어떤 관계가 있는지 분석하는 것
# 공분산을 표준화 한 것을 상관계수(r)라고 한다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

df = pd.DataFrame({'id1':(1,2,3,4,5), 'id2':(2,3,-1,7,9)})
print(df)
print(df.cov())     # 공분산 
print(df.corr())    # 피어슨 상관계수를 사용.

# plt.scatter(df.id1,df.id2)
# plt.show()


# 파일 자료를 읽어 상관분석
data = pd.read_csv("../testdata/drinking_water.csv")
print(data.head(3), len(data))
print(data.info())
print(data.describe())

# 공분산
print(np.cov(data.친밀도, data.적절성))   # np 는 2개씩 확인 가능
print(np.cov(data.친밀도, data.만족도))   
print(data.cov())       # pandas로는 한꺼번에 확인가능

# 상관계수
print(np.corrcoef((data.친밀도, data.적절성)))
print(np.corrcoef((data.친밀도, data.만족도)))
print(data.corr())                  # method 작성X 기본값은 'pearson'
print(data.corr(method='pearson'))  # 정규성, 연속형(등간, 비율 척도)
print(data.corr(method='spearman')) # 서열척도, 비선형
print(data.corr(method='kendall'))  # 서열척도, 비선형

print('-------------'*10)
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))    # sort 사용

# 시각화
# data.plot(kind='scatter', x='만족도', y='적절성')
# plt.show()
#
# from pandas.plotting import scatter_matrix
# attr=['친밀도','적절성','만족도']
# scatter_matrix(data[attr])
# plt.show()

# hitmap 
import seaborn as sns
# sns.heatmap(data.corr())
# plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()



