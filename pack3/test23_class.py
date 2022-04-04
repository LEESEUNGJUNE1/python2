# Class : 00P - 자원의 재활용 (포함, 상속 - 다형성 구사 )
# Class는 새로운 타입을 생성. 멤버 : 멤버변수(필드), 멤버 메소드. 접근지정자 x, Overloading x
# Class 선언 후 실행하면 객체가 생성(prototype)
from future.builtins.misc import isinstance

print(type(1))
print(type([]))

a=1

def func():
    pass

class TestClass:
    aa = 1 # 멤버 변수(필드)
    
    def __init__(self):
        print('생성자 : 초기화 담당')
        
    def __del__(self):
        print('소멸자 : 마무리 담당')
        
    def myMethod(self):
        name = "신기해" # 지역변수
        print("클래스 내에 있는 함수를 메소드 : self를 매개변수로 갖는다")
        print(name)
        print(self.aa)
        
print(TestClass.aa, id(TestClass))
#TestClass.myMethod()

test = TestClass() # 생성자를 호출하고 TestClass 타입의 객체가 생성
print(test.aa)
test.myMethod() # Bound method call
TestClass.myMethod(test) # unBound method call

print()
print(type(test))
print(isinstance(test, TestClass))
print(id(test), id(TestClass))