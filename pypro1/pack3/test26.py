# Class는 새로운 타입을 만든다.
class Singer:
    title_song = '좋은날'
    
    def sing(self):
        msg = "노래는"
        print(msg, self.title_song, '이이이~')
        
    def hello(self):
        print('안녕하세요 저 가수에요')
            
    # ...
    
# --- 아래 내용은 별도의 무듈을 만들었다 가정 ---
iu = Singer()
iu.hello()
iu.sing()

print()
blackpink = Singer()
blackpink.hello()
blackpink.sing()
blackpink.title_song = "마지막 처럼"
blackpink.sing()
blackpink.co = 'YG'
print('blackpink 소속사 : ', blackpink.co)

#print('bts 소속사 : ', iu.co)
iu.sing()


print()
print(id(iu), id(blackpink))
print(type(iu), type(blackpink))