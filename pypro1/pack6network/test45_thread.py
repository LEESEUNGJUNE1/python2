# Thread
# process는 실행 가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하며 task 라고도 부른다.
# process의 작은 실행 단위를 thread 라고 한다. thread 기법을 이용하면 여러개의 thread 통해 여러개의 작업을 할 수 있다.
# multi-thread에 의한 multi-tasking이 가능하다.

import threading, time

def run(id):
    for i in range(1,11):
        print('id:{}-->{}'.format(id,i))
        time.sleep(0.5)
        


# 1) thread X 사용하지 않음
# run('일')  # 순차적
# run('이')

# 2) thread O 사용 함
th1 = threading.Thread(target= run, args=('일',)) # target이 종료 되야 thread가 끝남
th2 = threading.Thread(target= run, args=('이',))
th1.start()  # tread 의 시작
th2.start()

th1.join()  # 사용자 정의 thread가 끝나기 전에 main thread는 끝나지 않는다
th2.join()  

print('프로그램 종료')







