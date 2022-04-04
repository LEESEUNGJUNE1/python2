# 자원의 재활용을 목적으로 클래스의 상속 - 다형성

class Animal:
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물')
    # ...

class Dog(Animal):
    #public Dog(){
        #super()
    #} => java에서 부모를 호출할때
    
    def __init__(self):
        print('Dog 생성자')

    def my(self):
        print('난 멍멍이라고 해요')

dog1 = Dog()
dog1.my()
dog1.move()

print()
class Horse(Animal):
    pass

horse = Horse()
horse.move()

