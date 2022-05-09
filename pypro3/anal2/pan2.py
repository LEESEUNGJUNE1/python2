from pandas import Series, DataFrame

data = Series([1,3,2], index = (1,4,2))    # index 는 tuple , set 가능
print(data)

data2 = data.reindex((1,2,4))              # 행순서 재배치
print(data2)

print('-----'*10)
data3 = data2.reindex([0,1,2,3,4,5])       # 대응 값이 없는 index는 결측값이 된다. 
print(data3)
print('-----'*10)
print(data2.reindex([0,1,2,3,4,5], fill_value = 777))  # 대응 값이 없는 index는 777로 채워진다.
print('-----'*10)
print(data2.reindex([0,1,2,3,4,5], method = 'ffill'))  # NaN 앞 값으로 현재 NaN 으로 대체한다.
print(data2.reindex([0,1,2,3,4,5], method = 'pad'))
print('-----'*10)
print(data2.reindex([0,1,2,3,4,5], method = 'bfill'))  # NaN 뒷 값으로 현재 NaN 으로 대체한다.
print(data2.reindex([0,1,2,3,4,5], method = 'backfill'))

print('-----'*10)
import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index=['1월','2월','3월','4월'], columns=['강남','강북','서초'])
print(df)
print(df['강남'])
print(df['강남'] > 3)
print(df[df['강남'] > 3])               # 조건이 참인 값만 나오게 하기
print('-----'*10)
df[df < 3] = 0                         # 3보다 작으면 0으로 바꾸기
print(df)  

print('슬라이싱 관련 method : loc() - 라벨 지원, iloc() - 숫자 지원 ----')
print(df['강남'])
# 복수 인덱싱 
print(df.loc['3월'])                   # 3월 행이 나온다.
print(df.loc['3월',])                  # 3월 행이 나온다.
print(df.loc['3월',:])                 # 3월 행이 나온다.
print('-----'*10)
print(df.loc[:'3월'])                  # 3월 이하 행 모든 열 출력 
print(df.loc[:'3월', ['서초']])         # 서초 행 출력 

print('-----'*10)
print(df.iloc[2])                      # 2행이 출력 
print(df.iloc[2, :])                   # 2행이 출력
print(df.iloc[:3])                     # 3 미만행 출력
print(df.iloc[:3,2])                   # 3 미만행 2열 출력
print(df.iloc[1:3,1:3])                # 1행 2열 출력 

print('---연산--------------------------')
s1 = Series([1,2,3], index = ['a','b','c'])
s2 = Series([4,5,6,7], index = ['a','b','d','c'])
print(s1)
print(s2)
print(s1 + s2)                         # index name 끼리 연산    -,*,/
print(s1.add(s2))                      # index name 끼리 연산    sub,mul,div

print('-----'*10)
df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('kbs'), index = ['서울','대전','부산'])          
df2 = DataFrame(np.arange(12).reshape(4,3), columns=list('kbs'), index = ['서울','대전','제주','광주'])
print(df1)
print(df2) 
print('-----'*10)
print(df1 + df2)                     # -,*,/
print(df1.add(df2,fill_value=0))     # NaN 은 0으로 채운다. sub,mul,div



