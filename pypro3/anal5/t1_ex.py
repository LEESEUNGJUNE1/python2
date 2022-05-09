import numpy as np
import scipy.stats as stats
import pandas as pd

# [one-sample t 검정 : 문제1]  
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
# 305 280 296 313 287 240 259 266 318 280 325 295 315 278

# 귀무 : 백열전구의 수명은 300시간이다.
# 대립 : 백열전구의 수명은 300시간이 아니다.
one_sample = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(one_sample).mean())      # 289.7857142857143 vs 300
# 정규성 확인
print(stats.shapiro(one_sample))        # pvalue=0.82086 > 0.05 이므로 정규성 만족
result = stats.ttest_1samp(one_sample, popmean=300)
print('t값:%.3f, p-value:%.3f'%result)   # 해석 : p-value:0.144 > 0.05 이므로 귀무가설 채택

print('-----------'*10)

# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")

# 귀무 : 노트북 평균 사용 시간이 5.2 시간 이다.
# 대립 : 노트북 평균 사용 시간이 5.2 시간이 아니다.
data2 = pd.read_csv("../testdata/one_sample.csv")
print(data2.head(100))
data2=data2.replace("     ", "")
data2.time=pd.to_numeric(data2.time)
data2=data2.dropna(how='all',axis=0)
data2=data2.dropna(axis=0)
print(data2['time'].mean())
# 정규성 확인
print(stats.shapiro(data2.time))                    # pvalue=0.72426 정규성 만족
print(stats.ttest_1samp(data2.time, popmean=5.2))   # pvalue=0.00014166 < 0.05 이므로 귀무가설 기각
print('t값:%.3f, p-value:%.5f'%result)               # p-value:0.14361

print('-----------'*10)

# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.

# 귀무 : 전국 평균 미용 요금이 15000원 이다.
# 대립 : 전국 평균 미용 요금은 15000원 아니다.
data3 = pd.read_excel("../testdata/pdata.xls").T.dropna().iloc[2:,]
data3.columns = ['미용']

print(np.mean(data3.미용))
result = stats.ttest_1samp(data3['미용'], popmean=15000)      # 16743 vs 15000 
print('t값:%.3f, p-value:%.5f'%result)                       # p-value:0.00118 < 0.05 귀무가설 기각



