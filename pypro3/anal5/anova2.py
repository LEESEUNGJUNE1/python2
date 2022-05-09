# 분산분석
# 강남구에 있는 GS 편의점 3개지역 알바생의 급여에 대한 평균차이를 검정

# 귀무 : GS 편의점 3개지역 알바생의 급여에 대한 평균에 차이가 없다.
# 대립 : GS 편의점 3개지역 알바생의 급여에 대한 평균에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats 
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

"""
data = pd.read_csv("../testdata/group3.txt", header=None)
print(data)    # <class 'pandas.DataFrame'>
print(data.describe())
"""

data = np.genfromtxt("../testdata/group3.txt", delimiter=",")
print(data[:3], type(data)) # <class 'numpy.ndarray'>
print(data.shape)   # (22, 2)

# 세 개의 집단에 급여 평균
gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]
print(gr1, ' ', np.mean(gr1))       # 316.625
print(gr2, ' ', np.mean(gr2))       # 256.444
print(gr3, ' ', np.mean(gr3))       # 278.0

# 정규성
print(stats.shapiro(gr1).pvalue)
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)

# 등분산성
print(stats.levene(gr1,gr2,gr3).pvalue)
print(stats.bartlett(gr1,gr2,gr3).pvalue)   # 표본의 수가 적으므로 비모수 검정 방법 (순서를 이용해서 계산하는 방법)

# 데이터 분포 시각화 
# plt.boxplot([gr1,gr2,gr3])
# plt.show()

# 일원분산분석 방법1 : anova_lm 는 statsmodels가 제공 
df = pd.DataFrame(data, columns = ['pay','group'])
print(df.head(3))

lmodel = ols('pay ~ C(group)',data = df).fit()
print(anova_lm(lmodel, typ=1))
# PR(>F) 0.043589 < 0.05 이므로 귀무 기각. GS 편의점 3개지역 알바생의 급여에 대한 평균에 차이가 있다.

print('-------------'*10)
# 일원분산분석 방법2 : f_oneway 는 scipy가 제공
f_statistic, pvalue = stats.f_oneway(gr1,gr2,gr3)
print('f_statistic : ', f_statistic)
print('pvalue : ', pvalue)

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd 
turkey_result = pairwise_tukeyhsd(endog = df.pay, groups=df.group)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()


