# 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다.
# 'eat_out.txt' 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시한다.
# ① 소스 코드와 모델의 분류정확도를 출력하시오.
# ② 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하시오.

#조건1 : 모델 생성은 glm 함수를 사용하도록 한다.
#조건2 : 키보드로 입력할 소득 수준 값은 45로 한다. (배점:10)

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.metrics import accuracy_score

data = pd.read_csv('../testdata/eat_out.txt')
print(data)
eatout = data[(data.요일 == '토')| (data.요일 == '일')]
print(eatout)

formula = '외식유무 ~ 소득수준'
result = smf.glm(formula = formula, data = eatout, family = sm.families.Binomial()).fit()  # binomial 을 넣기 때문에 이항분포가 된다
print(result)
print(result.summary())

pred = result.predict(eatout)
print('정확도: ', accuracy_score(eatout['외식유무'], np.around(pred)))

key = int(input('소득 수준 입력 : '))
newdf = pd.DataFrame({'소득수준':[key]})
pred2 = result.predict(newdf)
print(np.rint(pred2.values))