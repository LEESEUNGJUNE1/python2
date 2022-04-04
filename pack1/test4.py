# 정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다.
import re

ss = "1234 abc가나다abcABCfun_123555_6 Python if fun"
print(ss)
print(re.findall('123', ss))
aa = re.findall(r'\n123', ss)
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('\d\d', ss)) #\D \s \S \w \W
print(re.findall('[0-9]+', ss)) # 1회 이상
print(re.findall('[0-9]?', ss)) 
print(re.findall('[0-9]*', ss))
print(re.findall('[0-9]{2}', ss))
print(re.findall('[0-9]{2,3}', ss))
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-Z]', ss))
print(re.findall('[가-힣]', ss))
print(re.findall('[^가-힣]', ss))
print(re.findall('.bc', ss))
print(re.findall('a..', ss))
print(re.findall('^123', ss))
print(re.findall('fun$', ss))
print(re.findall('12|34', ss))
print(re.findall('(ab)+(c)', ss))

p = re.compile('abc')
print(re.findall(p, ss))

p = re.compile('the', re.IGNORECASE)
print(p.findall('The DoG the dog'))




