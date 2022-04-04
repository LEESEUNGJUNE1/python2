# 사용자 정의 모듈 작성 및 읽기
a = 10
print(a + 10)
print('작업을 하다가 외부 모듈 읽기')
print(dir())

list1 = [1,3]
list2 = [2,4]

import pack2.mymod1 # 패키지명.모듈명
pack2.mymod1.listHap(list1,list2)
#print(dir())

def listTot(*ar):
    print(ar)
    
    if __name__ == '__main__':
        print('이 파일이 메인임을 선언!')

listTot(list1,list2)

print()
from pack2.mymod1 import kbs
kbs()

from pack2.mymod1 import mbc, price
mbc()
print('price : ', price)

import other.mymod2
print(other.mymod2.Hap(5, 3))

from other.mymod2 import Cha
print(Cha(5,3))

import mymod3
print(mymod3.Gop(5, 3))

from mymod3 import Nanugi
print(mymod3.Nanugi(5, 3))