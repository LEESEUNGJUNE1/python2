# 1) step1 : array 관련 문제
# 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
# < 출력 결과 예시>
# 1행 합계   : 0.8621332497162859
# 1행 최댓값 : 0.3422690004932227
# 2행 합계   : -1.5039264306910727
# 2행 최댓값 : 0.44626169669315
# 3행 합계   : 2.2852559938172514
# 3행 최댓값 : 1.5507574553572447
import numpy as np
np.random.seed(1)
a = np.random.randn(5, 4)  # 정규 분포
print(a)
for i in range(1, 4):
    print(i,'행 합계 : ', sum(a[i]))
    print(i,'행 최대값 : ', max(a[i]))
    i += 1
    
# 2) step2 : indexing 관련문제
b = np.zeros((6,6))
print(b)
b = np.arange(1, 37).reshape(6, 6)
print(b)
print(b[1, :])
print(b[:, 4])
print(b[2:5, 2:5])

import random
c = np.zeros((6,4))
print(c)
for i in range(0, 6):
    c[i, 0] = random.randint(20, 100)
    for j in range(0, 4):
        c[i, j] = c[i, 0] + j
        j += 1
    i += 1
print(c)
c[0] = np.array([1000, 1000, 1000, 1000])
c[5] = np.array([6000, 6000, 6000, 6000])
print(c)

# 3) step3 : unifunc 관련문제
d = np.random.randn(4, 5)
print(d)
print('평균:', np.mean(d))
print('합계:', np.sum(d))
print('표준편차:', np.std(d))
print('분산:', np.var(d))
print('최대값:', np.max(d))
print('최소값:', np.min(d))
print('1사분위 수:', np.percentile(d, 25))
print('2사분위 수:', np.percentile(d, 50))
print('3사분위 수:', np.percentile(d, 75))
print('요소값 누적합:', np.cumsum(d))