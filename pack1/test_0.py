# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
from pack1.test1 import aa
i=1; hap=0
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        # print(i)
        hap += i
    i += 1
print('합은',hap) # 합은 867

# 문2) 2 ~ 5 까지의 구구단 출력
print('문2, 구구단 2~5까지')
i = 1
while i < 5:
    i = i + 1
    j = 1
    while j < 10:
        print(i, 'X', j, '=', i*j)
        j = j + 1

# 문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
print()
i = -1
hap = 0
while 1:
    hap += i
    if i<0:
        i = i*(-1)+2
    else :
        i = i*(-1)-2
    if i == -101:
        break

print('합은',hap)

# 문제 4번
aa = 2; count = 0
while aa <= 1000:
    imsi = False
    bb = 2
    while bb <= aa - 1:
        if aa%bb == 0:
            imsi = True
        bb += 1
        
    if imsi == False:
        print(aa, end = '')
        count += 1
        
    aa += 1
    
print('갯수 : ',count)













