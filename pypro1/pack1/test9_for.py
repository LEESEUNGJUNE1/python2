# 반복문 for
# 웹에서 읽은 자료라 가정 : 단어 수 출력 ex) 모터를 :3
ss = """
하이브리드 차는 내연기관과 배터리로 움직이는 모터를 동시에 탑재한 차량이다.
엔진이 아예 없는 전기차와 가장 큰 차이점은 충전할 필요가 없다는 점이다.
이런 분위기 속에 한때 수입 항리브리드차의 대표 주자였던 넥소 에 대한 관심도 높아지고 있다.
넥소는 여러 차례 월 기준 수입차 판매 1위를 차지했을 정도로 인기가 많다.
넥쏘는 최근 많이 출시되고있는 마일드 하이브리드 차량과 달리 배터리(모터)만으로 차량 구동이 가능한 정통 하이브리드 차다.
마일드 하이브리드는 내연기관 차량에 48볼트(v) 배터리와 모터를 추가 장착한 형태로 전기 모터만으로는 차량 구동이 불가능 하다.
엔진이 중심이 되고 모터와 배터리는 주행 효율을 높여주는 수준의 하이브리드 라는 의미다.
엔진이 아예 없는 전기차와 가장 큰 차이점은 충전할 필요가 없다는 점이다."""

import re

ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3 = ss2.split(sep=' ')
print(ss3)
print(len(ss3))
print(len(set(ss3)))

cou = {} # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        pass
    else:
        cou[i] = 1 # {'키':i}
print(cou)

print()
for test in ['111-1234','일이삼-사오육칠','222-3333']:
    if re.match(r'^\d{3,4}-\d{4}',test):
        print(test)
    else:
        print('전화번호 ㅜㅠ')
        
print()
a=1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
        
print()

print(list(i for i in a if i % 2 == 0))

print()
datas = [1,2,'a',True,3.4]
li = [i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,3}
se = {i * i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id = {value:key for key, value in id_name.items()}
print(name_id)

print()
temp = [1,2,3]
for i in temp:
    print(i, end =' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
# 과일 값 계산
price = {'사과':2000, '오렌지':1000,'배':3000}
guest={'사과':2, '배':1}
bill = sum(price[f] * guest[f] for f in guest) # sum(요소들) : 합을 구하는 내장 함수
print(bill)