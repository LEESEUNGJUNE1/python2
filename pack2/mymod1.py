# 사용자 정의 모듈 : 독립적으로 사용하지않고 다른 모델에서 호출될 대상
price = 12345

def listHap(*ar):
    print(ar)
    if __name__ == '__main__':
        print('이 파일이 메인이야~')

def kbs():
    print('국민의 방송 KBS')
def mbc():
    print('만나면 좋은 친구 : 11')