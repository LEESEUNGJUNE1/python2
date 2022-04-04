# 함수 작성
from pack1.test11_func import res
a = 1
b = a + 1
# 어쩌구 저쩌구 하다가 모듈의 멤버로 함수 선언

def Dofunc1():
    print('Dofunc1 수행')
    
c = b + 20

# 함수호출
Dofunc1() # 함수 호출
# 딴짓하다가...
res = Dofunc1() # 함수 호출
print(res)
print(Dofunc1())

print(Dofunc1())
print(id(Dofunc1()))
print(id(print))
print(id(sum))
print(id(c))

d=c               # 주소 치환
Dofunc2 = Dofunc1 # 주소 치환
Dofunc2()

print('-----')
def doFunc3(arg1, arg2):
    res = arg1 + arg2
    #return res
    return res
    if res % 2 == 1:
        return
    else:
        return res

print('결과는 ', doFunc3(10, 20))
aa = doFunc3(10,21)
print('결과는 ', aa)

print('-----')
def area_tri(a,b):
    c = a * b / 2
    aria_print(c)

def aria_print(c):
    print('삼각형의 면적은 ' + str(c))
    
area_tri(5, 6)

print('-----')
def func1():
    print('func1 멤버 처리')
    def func2():
        print('func2 멤버 처리 : 내부 함수')
    func2()
func1()

print('-----')
def swap(a,b):
    return b,a # tuple로 반환

a=10; b=20
c = swap(a, b)
print(c)
print(c[0], c[1])

print('----')
def isOdd_func(arg):
    return arg % 2 == 1

mydict = {x:x * x for x in range(11) if isOdd_func(x)}
print(mydict)

print('**********')
print('현재 파일(모듈)의 객체 목록 : ', globals())
print(dir(__builtins__))



print('프로그램 종료')