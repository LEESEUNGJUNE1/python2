# 완성차 : 여러 개의 부품 클래스를 이용해 완성차를 생산

import pack3.test27_handle

class PohamCar():
    turnShowMessage = "정지"
    
    def __init__(self,ownerName):
        self.ownerName = ownerName
        self.handle = pack3.test27_handle.PohamHandle() # 클래스의 포함관계
        
    def TurnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.RightTurn(q)
        elif q < 0:
            self.turnShowMessage = self.handle.LeftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직진'
            self.handle.quantity = 0

if __name__ == '__main__':
    tom = PohamCar('미스터 톰')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    
    tom.TurnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    
    print()
    sujan = PohamCar('미스 수진')
    sujan.TurnHandle(-15)
    print(sujan.ownerName + '의 회전량은 ' + sujan.turnShowMessage + str(sujan.handle.quantity))
    