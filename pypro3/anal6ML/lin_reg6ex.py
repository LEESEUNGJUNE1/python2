# 회귀분석 문제 3) 
# kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.rcParams['axes.unicode_minus']=False

cseat = pd.read_csv("../testdata/Carseats.csv")
print(cseat.head(3), cseat.shape)   # (400, 11)
print(cseat.info())
print(cseat.corr())

column_select = "+".join(cseat.columns.difference(['Sales']))
print(column_select)
lm = smf.ols(formula='Sales ~ Income + Advertising + Price + Age', data = cseat).fit()
print('요약 결과 : ', lm.summary())

print('--------------새로운 값으로 예측---------------------')
new_cseat = pd.DataFrame({'Income':[35,62,24], 'Advertising':[6,3,11],'Price':[105,89,75],'Age':[32,54,22]})
pred = lm.predict(new_cseat)
print('Sales 예측값 : \n',pred)

# 잔차항
fitted = lm.predict(cseat)
residual = cseat['Sales'] - fitted
print(residual[:3])
print('잔차의 평균:' ,np.mean(residual)) # -8.057998712729386e-15

import seaborn as sns
print('선형성 : 예측값과 실제값의 잔차가 일정하게 분포')
sns.regplot(fitted, residual, lowess = True, line_kws={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0])
plt.show()


# print('상관계수(r) : ', cseat.loc[:,['Sales','CompPrice']].corr())              # Sales 와 CompPrice 의 상관관계           0.064
# print('상관계수(r) : ', cseat.loc[:,['Sales','Income']].corr())                 # Sales 와 Income 의 상관관계              0.151
# print('상관계수(r) : ', cseat.loc[:,['Sales','Advertising']].corr())            # Sales 와 Advertising 의 상관관계         0.269
# print('상관계수(r) : ', cseat.loc[:,['Sales','Age']].corr())                    # Sales 와 Age                       -0.231815
# print('상관계수(r) : ', cseat.loc[:,['Sales','Education']].corr())              # Sales 와 Education                 -0.051955
#
# lm = smf.ols(formula = 'Sales ~ Advertising', data = cseat).fit()
# print(lm.summary())     # Prob (F-statistic): 4.38e-08  R-squared: 0.073
# print('설명력 : ' , lm.rsquared)
# print('p-values : ' , lm.pvalues[1])    # 4.377677110302928e-08 < 0.05
#
# plt.scatter(cseat.Advertising, cseat.Sales)
# plt.xlabel('Advertising')
# plt.ylabel('Sales')
# x = pd.DataFrame({'Advertising':[cseat.Advertising.min(),cseat.Advertising.max()]})   
# y_pred = lm.predict(x)
# plt.plot(x, y_pred, c='red')
# plt.show()
#
# c_new = pd.DataFrame({'Advertising':[300.12, 66.55, 30]})
# print(c_new)
#
# pred_new = lm.predict(c_new)
# print('광고 Sales 추정치: ', pred_new.values)
# print(cseat.corr()) 
#
# lm_mul = smf.ols(formula = 'Sales ~ Advertising + Income', data = cseat).fit()
# print(lm_mul.summary())     # Adj. R-squared: 0.087    Prob (F-statistic): 5.69e-09 < 0.05 유의한 모델
#
#
# c_new2 = pd.DataFrame({'Advertising':[220.12, 55.66, 10], 'Income':[30.3,40.4,50.5]})
# pred_new2 = lm.predict(c_new2)
# print('Sales 추정치 : ', pred_new2.values)
#
# fitted = lm_mul.predict(cseat.iloc[:, 0:2])
# print(fitted)