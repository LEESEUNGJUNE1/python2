# class

kor = 100

def abc():
    print('함수라고 해')

class MyClass:
    kor = 90
    
    def abc(self):
        print('난 메소드야~')
        
    def show(self):
        # kor = 88
        print(self.kor)
        print(kor)
        self.abc()
        abc()

my = MyClass()
my.show()

print('-------')
class OurClass:
    a = 1
    
print(OurClass.a)

our1 = OurClass()
print(our1.a)

our2 = OurClass()
print(our2.a)
our2.b = 2
print(our2.b)

print(our1.b)