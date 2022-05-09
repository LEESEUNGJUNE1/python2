# two-way anova(이원 분산분석 - 요인이 두 개)

import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import urllib.request
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.rc('font', family=('malgun gothic'))

url = "https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3_2.txt"
data = pd.read_csv(urllib.request.urlopen(url))     # urllib.request 을 이용해서 url 읽기
print(data.head(3), data.shape)     # (36, 3)

# data.boxplot(column='머리둘레', by='태아수', grid=False)
# plt.show()

# 귀무 : 태아수와 관측자수는 태아의 머리둘레와 관련이 없다. (머리둘레의 평균과 차이가 없다.)
# 대립 : 태아수와 관측자수는 태아의 머리둘레와 관련이 있다. (머리둘레의 평균과 차이가 있다.)

# 상호 작용을 주지 않은 경우
reg = ols("data['머리둘레'] ~ C(data['태아수']) + C(data['관측자수'])", data = data).fit()
result = sm.stats.anova_lm(reg, typ=2)
print(result)

print('----------'*10)
# 상호 작용이 있는 경우
formula = "머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)"
reg2 = ols(formula, data).fit()
result2 = sm.stats.anova_lm(reg2, typ=2)
print(result2)
# PR(>F) 3.295509e-01 > 0.05 귀무가설 채택
# 태아수와 관측자수는 태아의 머리둘레와 관련이 없다.
