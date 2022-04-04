# 메소드 오버라이드 : 다형성

class Parent:
    def printData(self):
        pass

class Child1(Parent):
    def printData(self):
        print('Child1 에서 Overrinde')

class Child2(Parent):
    def printData(self):
        print('Child2 에서 재정의')
        print('부모 메소드와 이름은 같으나 기능이 다름') 

    def abc(self):
        print('child2 고유 메소드')

c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
c2.abc()
 
print('\n다형성 ---')
# par = Parent()
par = c1
par.printData()
print()
par = c2
par.printData()
par.abc()

print()
plist = [c1, c2]
for a in plist:
    a.printData()