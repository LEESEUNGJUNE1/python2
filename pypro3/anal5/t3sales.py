# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 강수 여부에 따른 매출의 평균에 차이를 검정

# 비가 올 때의 매출액
# 비가 안올 때의 매출액

# 귀무 : 강수량에 따른 매출액에 차이가 없다.
# 대립 : 강수량에 따른 매출액에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

# 자료 읽기1
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype={'YMD':'object'})    # int를 object으로 변환 type을 맞추기 위해서
print(sales_data.head(3))
print(sales_data.info())

print('----------'*10)
# 자료 읽기2
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-','')) # -을 제거 2018-06-01 -> 20180601
print(wt_data.head(3))
print(wt_data.info())

print('----------'*10)
# 두 파일을 병합
frame = sales_data.merge(wt_data,how='left',left_on='YMD',right_on='tm')    # merge하기 , sales_data 기준으로 YMD 와 tm merge
print(frame.head(5))
print(len(frame))
print(frame.columns)

data = frame.iloc[:, [0,1,7,8]]     # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3), len(data))      # 328 행
print(data.isnull().sum())          # 결측치 없음

print('독립표본 t검정 -----강수 여부에 따른 매출액의 평균에 차이가 있는가? ---------------')
#print(data['sumRn'] > 0)            # False,True ...

# data['rain_yn'] = (data['sumRn'] > 0).astype(int)   # 비옴 : 1, 비안옴 : 0
# print(data.head(3))

# print(True * 1, False * 1)  # 1 0
data['rain_yn'] = (data.loc[:, ('sumRn')] > 0) * 1     # 비옴 : 1, 비안옴 : 0
print(data.head(3))

# 시각화
import matplotlib.pyplot as plt

sp = np.array(data.iloc[:, [1, 4]])
print(sp[:2])   # [[    0     0]  [18000     1]]
tg1 = sp[sp[:, 1] == 0, 0]  # 비 안올 때 매출액
tg2 = sp[sp[:, 1] == 1, 0]  # 비 올 때 매출액
print(tg1[:3])
print(tg2[:3])

# plt.plot(tg1)
# plt.show()
# plt.plot(tg2)
# plt.show()

# 두 집단의 각 평균
print('비 안올 때 : ', np.mean(tg1), ', 비 올 떄 : ', np.mean(tg2))   # 761040.2542372881 vs 757331.5217391305

plt.boxplot([tg1,tg2], notch=True, meanline = True, showmeans=True)
plt.show()

# 정규성
print(len(tg1),len(tg2))
print(stats.shapiro(tg1).pvalue)    # 0.0560494 > 0.05 만족
print(stats.shapiro(tg2).pvalue)    # 0.8827397 > 0.05 만족 

# 등분산성
print(stats.levene(tg1,tg2).pvalue) # 0.7123452 > 0.05 만족

print(stats.ttest_ind(tg1,tg2, equal_var = True))
# Ttest_indResult(statistic=0.10109828602924716, pvalue=0.919534587722196)
# 해석 : pvalue=0.9195 > 0.05 이므로 귀무가설 채택
# 강수량에 따른 매출액의 평균의 차이는 없다.




 
