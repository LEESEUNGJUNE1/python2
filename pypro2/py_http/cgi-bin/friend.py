import cgi

form = cgi.FieldStorage()
name = form["name"].value
phone = form["phone"].value
gen = form["gen"].value

print('content-Type:text/html;charset=utf-8\n')
print('''
<html>
<head>
<meta charset="UTF-8">
<title>friend</title>
</head>
<body>
<h2>친구 정보</h2>
이름은 : {0}, 연락처는 : {1}, 성별 : {2}
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(name, phone, gen))