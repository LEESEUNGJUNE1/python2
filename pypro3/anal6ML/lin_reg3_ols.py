# ols 사용 : 가장 기본적인 결정론적 선형회귀방법. 불확실성이 있다. 

import pandas as pd
import statsmodels.formula.api as smf
df = pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3))
print(df.corr())

# 회귀분석 : "만족도와 적절성은 인과관계가 있다" 라는 가정하에 
model = smf.ols(formula = '만족도 ~ 적절성', data=df).fit()
print(model.summary())
print(0.766853 ** 2)

print('결정계수 : ', model.rsquared)    # 결정계수 만 볼 수 있다.
print('p-values : ', model.pvalues)   # p-values만 볼 수 있다.
print('예측값 : ', model.predict()[:5])
print('실제값 : ', df.만족도[:5].values)

# 시각화
import numpy as np
import matplotlib.pyplot as plt
plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도,1)
plt.plot(df.적절성, df.적절성 * slope + intercept, 'b')
plt.show()



