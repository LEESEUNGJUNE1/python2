# 파일 단위로 읽고 저장
import os

print(os.getcwd())

try:
    print('파일 읽기') # mode = 'r', 'w', 'a', |+'b'
    # f1 = open(r'C:\work\psou\pypro1\pack4\abc.txt', mode='r', encoding='utf-8')
    #f1 = open(os.getcwd() + r'C:\abc.txt', mode='r', encoding='utf-8')
    f1 = open('abc.txt', mode='r', encoding='utf-8')
    print(f1)
    print(f1.read())
    f1.close()

    print('파일 저장')
    f2 = open('abc2.txt', mode='w', encoding='utf-8') # a = 추가
    f2.write('my friend\n')
    f2.write('tom, 한국인')
    f2.close()
    print('저장 성공')

    print('파일 추가')
    f3 = open('abc2.txt', mode='a', encoding='utf-8') # w = 덮어쓴다.
    f3.write('\n비니시우스')
    f3.write('\n벤제마')
    f3.write('\n아센시오')
    f3.close()
    print('추가 성공')
    
    print('파일 읽기')
    f4 = open('abc2.txt', mode='r', encoding='utf-8')
    print(f4.readline())
    print(f4.read())
    f4.close()

except Exception as e:
    print('에러 : ', e)

print('파일 처리 계속 --- with 문 사용')

try:
    with open('abc3.txt', mode = 'w', encoding = 'utf-8') as ff1:
        ff1.write('파이썬으로 문서 저장\n')
        ff1.write('with 문을 사용하면\n')
        ff1.write('명시적으로 close()할 필요가 없다\n') # with문이 알아서 해주기 때문
    print('저장 완료')
    
    with open('abc3.txt', mode = 'r', encoding = 'utf-8') as ff2:
        print(ff2.read())

except Exception as e2:
    print('에러2 : ' + str(e2))

print('파일 처리 계속 --- pickle 모듈 사용 : 객체를 파일로  저장') #object로 저장하고 읽을수 있다.
import pickle

try:
    dictData = {'tom':'111-1111', 'james':'222-2222'} # 중요데이터를 파일로 저장해서 다른사람에게 줄때 사용
    listData = ['모드리치','크로스']
    tupleData = (dictData, listData)

    with open(file = 'hello.data', mode = 'wb') as ff3: # w'b'는 encoding이 필요하지 않다.
        pickle.dump(tupleData, ff3)
        pickle.dump(listData, ff3)

    print('객체를 파일로 저장')

    with open(file = 'hello.data', mode = 'rb') as ff4:
        a, b = pickle.load(ff4)
        print(a)
        print(b)
        c = pickle.load(ff4)
        print(c)

except Exception as e3:
    print('에러3 : ' + str(e3))