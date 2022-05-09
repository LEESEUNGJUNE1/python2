import numpy as np
import scipy.stats as stats
import pandas as pd
import MySQLdb
import pickle

# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

try:
    with open('mydb.dat',mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('연결오류:',e)
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_name,buser_num,buser_name,jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no 
    """
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), columns=['이름','부서번호','부서명','연봉'])
    print(df) 
    jik_ypay = df.groupby(['부서명'])['연봉'].mean()
    print(jik_ypay)     # 영업부 : 4908  vs  총무부 : 5414
    
    buser1 = df[df['부서명']=='총무부'].연봉
    buser2 = df[df['부서명']=='영업부'].연봉
    print(np.average(buser1),' ',np.average(buser2))
   
except Exception as e:
    print('처리오류:',e)
finally:
    cursor.close()
    conn.close()

# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
#    중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
#
#    기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?
# 귀무 : 학급의 학업능력이 변화했다고 볼 수 없다.
# 대립 : 학급의 학업능력이 변화했다고 볼 수 있다.

middle = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(middle))  # 74
print(np.mean(final))   # 81

print(stats.ttest_rel(middle, final))
# Ttest_relResult(statistic=-2.6281127723493993, pvalue=0.023486192540203194)
# 해석 : pvalue=0.02348 < 0.05 이므로 귀무가설 기각
# 

