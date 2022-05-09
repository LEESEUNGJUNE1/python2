import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
import MySQLdb
import pickle
import numpy as np

# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

data = {'종류':[1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
        '기름':[64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]}
df = pd.DataFrame(data)
print(df,type(df))
df = df.fillna(df['기름'].mean())
print(df)

# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 없다.
# 대립 : 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있다.
try:
    with open('mydb.dat', mode = 'rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ', e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select buser_name,jikwon_pay 
        from jikwon inner join buser
        on buser_num=buser_no
    """
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), 
                       columns = ['부서명','연봉'])
    print(df.groupby(['부서명']).mean(['연봉']))
    
    buser1 = df[df['부서명']=='총무부'].연봉    # 5414
    buser2 = df[df['부서명']=='영업부'].연봉    # 4908
    buser3 = df[df['부서명']=='전산부'].연봉    # 5328
    buser4 = df[df['부서명']=='관리부'].연봉    # 6262
    
    print(np.average(buser1),' ',np.average(buser2),' ',np.average(buser3),' ',np.average(buser4))
    
    # 정규성 검증
    print(stats.shapiro(buser1).pvalue)     # 0.026044 < 0.05
    print(stats.shapiro(buser2).pvalue)     # 0.025608 < 0.05
    print(stats.shapiro(buser3).pvalue)     # 0.419407 > 0.05
    print(stats.shapiro(buser4).pvalue)     # 0.907802 > 0.05
    
    print('--------------'*10)
    # 등분산성
    print(stats.levene(buser1,buser2,buser3,buser4).pvalue)
    print(stats.bartlett(buser1,buser2,buser3,buser4).pvalue) # 0.6290955395410989
    
    print('--------------'*10)
    # 일원분산분석
    f_statistic, pvalue = stats.f_oneway(buser1,buser2,buser3,buser4)
    print('f_statistic : ', f_statistic)
    print('pvalue : ', pvalue)  # pvalue :  0.74544 > 0.05 이므로 귀무가설 채택. 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 없다.
    
    
except Exception as e:
    print('오류 : ', e)
finally:
    cursor.close()
    conn.close()

print()





