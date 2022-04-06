# 웹용 파이썬 모듈 : 요청시 정보를 달고 넘어온다.
import cgi

form = cgi.FieldStorage()
name = form['name'].value
age = form['age'].value

print('content-Type:text/html;charset=utf-8\n')
print('''
<html>
<head>
<meta charset="UTF-8">
<title>my</title>
</head>
<body>
<h2>반가워요</h2>
이름은 : {0}, 나이는 : {1}
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(name, age))