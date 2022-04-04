# 우편번호 data 파일 사용
# 키보드로 동이름을 입력해서 해당 동이름의 자료만 읽기

try:
    dong = input('동이름 입력: ')
    # dong = '망원'
    # print(dong)
    
    with open(r'zipcode.txt', mode= 'r', encoding = 'euc-kr') as f:
        line = f.readline()
        #print(line)
        
        while line:
            # lines = line.split('\t')   # tab
            lines = line.split(chr(9))    # tab 으로 구분 by ascii code
            
            # print(lines)
            if lines[3].startswith(dong):
                print('[' + lines[0] + '] '+ lines[1] + ' ' + \
                      lines[2] + ' '+lines[3] + ' '+lines[4])
                
            line = f.readline()
        
except Exception as e:
    print('에러 :' ,e)