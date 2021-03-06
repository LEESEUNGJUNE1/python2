# 카이제곱검정 중 일원카이제곱 : 변인 단수 (관찰값이 1개)
# : 관찰도수가 기대도수와 일치하는 지를 검정하는 방법
# : 종류 : 적합도/선호도 검정
# - 범주형 변수가 한 가지로, 관찰도수가 기대도수에 일치하는지 검정한다.
# 주사위 눈금  1  2  3   4   5   6
# 관측도수    4  6  17  16  8   9    : 60회
# 기대도수   10  10 10  10  10  10   : 60회

# 적합도 검정
# : 자연현상이나 각종 실험을 통해 관찰되는 도수들이 귀무가설 하의 분포(범주형 자료의 각 수준별 비율)에 얼마나 일치하는가에 대한
# 분석을 적합도 검정이라 한다.
# : 관측값들이 어떤 이론적 분포를 따르고 있는지를 검정으로 한 개의 요인을 대상으로 함.

# <적합도 검정실습>
# 주사위를 60 회 던져서 나온 관측도수 / 기대도수가 아래와 같이 나온 경우에 이 주사위는 적합한 주사위가 맞는가를 일원카이제곱 검정
# 으로 분석하자.

# 귀무가설 : 기대치와 관찰치는 차이가 없다. 이 주사위는 게임에 적합하다.
# 대립가설 : 기대치와 관찰치는 차이가 있다. 이 주사위는 게임에 적합하지 않다.

import pandas as pd
import scipy.stats as stats
data = [4, 6, 17, 16, 8, 9]     # 관측값 
#data = [11, 5, 10, 13, 10, 11]     # 관측값 

print(stats.chisquare(data))
result = stats.chisquare(data)
print('검정통계량 X² 값:%.5f, p-value:%.5f'%(result))
print(result.statistic, result.pvalue)

exp = [10, 10, 10, 10, 10, 10]
print(stats.chisquare(data, exp))

# 결과 해석 : 유의확률(p-value) 0.01439 < 유의수준 0.05 이므로 귀무가설을 기각하고 대립가설을 채택한다.
# 다시 말해서 검정에 사용된 data 값은 우연히 발생된 값이 아니라 어떠한 필연적 원인에 의해 발생된 데이터라고 할 수 있다.
# 이 주사위는 게임에 적합하지 않다.

# 결과 얻기 2 - 카이제곱 분포표 사용
# 검정통계량 X² 값:14.20000, df: (N(6)-1) = 5, 임계값: 11.07 이므로 귀무가설을 기각하고 대립가설을 채택한다. 

print('---------------' *10)
# <선호도 분석 실습>
# 5개의 스포츠 음료에 대한 선호도에 차이가 있는지 검정하기

data2 = pd.read_csv("../testdata/drinkdata.csv")
print(data2)

# 귀무 : 스포츠 음료의 선호도에 차이가 없다.
# 대립 : 스포츠 음료의 선호도에 차이가 있다.
print(stats.chisquare(data2['관측도수']))
# statistic=20.488188976377952, pvalue=0.00039991784008227264
# 해석 : pvalue=0.000399917 < 0.05 귀무가설 기각
# 그러므로 이 결과를 바탕으로 향후 어떠한 조치를 취하는 데 있어 참고자료로 쓰인다.


