# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 온도 높낮이에 따른 매출의 평균에 차이를 검정

# 온도가 더울 때, 보통일 때, 낮을 때의 매출액

# 귀무 : 매출액은 온도에 영향이 없다.
# 대립 : 매출액은 온도에 영향이 있다.

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

print('----------'*10)
# 일변 최고 온도를 구간 설정
print(data.maxTa.describe())
import matplotlib.pyplot as plt
# plt.boxplot(data.maxTa)
# plt.show()

data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37],labels=[0, 1, 2])
print(data.head(3),' ', data['ta_gubun'].unique())

# 상관분석
print(data.corr())

x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(x1[:3])
print(x2[:3])

# 등분산성
print(stats.levene(x1,x2,x3))   # pvalue=0.03900 < 0.05 만족 X

# 정규성
print(stats.ks_2samp(x1, x2).pvalue)
print(stats.ks_2samp(x1, x3).pvalue)
print(stats.ks_2samp(x2, x3).pvalue)    # 만족 X 

print('----------'*10)
# 세 그룹의 매출액 평균
spp = data.loc[:, ['AMT', 'ta_gubun']]
print(spp.groupby('ta_gubun').mean())   # groupby 이용

print(pd.pivot_table(spp, index=['ta_gubun'], aggfunc='mean'))  # pivot_table 이용
print(spp[:3])

sp = np.array(spp)
group1 = sp[sp[:,1] == 0, 0]
group2 = sp[sp[:,1] == 1, 0]
group3 = sp[sp[:,1] == 2, 0]

# 매출액 시각화
# plt.boxplot([group1,group2,group3])
# plt.show()

# 일원분산분석
print(stats.f_oneway(group1,group2,group3))
# F_onewayResult(statistic=99.1908012029983, pvalue=2.360737101089604e-34)
# pvalue=2.360737101089604e-34 < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다.

print('----------'*10)
# 정규성 만족 X 
print(stats.kruskal(group1,group2,group3))      # kruskal-wallis test
# pvalue=1.5278142583114522e-29) < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다.

print('----------'*10)
# 등분산성 만족 X
# pip install pingouin
from pingouin import welch_anova
print(welch_anova(data = data, dv='AMT', between='ta_gubun'))
# pvalue= 7.907874e-35 < 0.05 이므로 귀무가설 기각. 매출액은 온도에 영향이 있다.

# 해석 : 날씨(온도 : 더움, 보통, 추움)에 의해 매출액의 차이가 있다.

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd 
turkey_result = pairwise_tukeyhsd(endog = spp['AMT'], groups=spp['ta_gubun'], alpha=0.05)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show() 
