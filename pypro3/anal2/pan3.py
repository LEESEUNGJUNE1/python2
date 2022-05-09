# 함수
from pandas import Series, DataFrame
import numpy as np

df = DataFrame([[1.4,np.nan],[7,4.5],[np.NaN, np.NaN],[0.5,-1]])
df.columns = ['one','two']
print(df)
print(df.drop(1))    # 특정 행 삭제
print(df.isnull())   # NaN 탐지
print(df.notnull())  # NaN 탐지
print(df.dropna())   # NaN 행 삭제 
print(df.dropna(how='any'))         # 열 값 중 하나라도 NaN인 경우 행 삭제 
print(df.dropna(how='all'))         # 열 값 모두가 NaN인 경우 행 삭제
print(df.dropna(subset=['one']))    # 특정열 값 중 NaN인 경우 행 삭제
print(df.dropna(axis='rows'))       # NaN이 포함된 행 삭제 
print(df.dropna(axis='columns'))    # NaN이 포함된 열 삭제

print(df.fillna(0))                 # NaN을 0으로 채운다. 평균 또는 대표값으로 채울 수도 있다. 

print('-----'*10)
print(df)
print(df.sum())                     # 기본이 열의 합
print(df.sum(axis=0))               # 열의 합 
print('-----'*10)
print(df.mean(axis=1))              # 행의 평균 

print('-----'*10)
print(df.max(axis=0))
print(df.idxmax())
print('-----'*10)
print(df.describe())                # 요약 통계량 
print(df.info())                    # 구조 확인

words = Series(['봄','여름','봄'])
print(words.describe())
# words.info()                      AttributeError: 'Series' object has no attribute 'info'

