from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request): # 클라이언트의 요청을 처리 하기위해 꼭 필요
    #return HttpResponse('요청 처리 결과')

    msg = '장고 만세'
    ss = "<html><body>장고 프로젝트 구현 %s</body></html>" %msg
    return HttpResponse(ss)

def showFunc(request):
    msg = '파이썬 어쩌구 저쩌구'
    
    return render(request, 'show.html', {'mymsg':msg}) # forward 방식 (서버에서 서버의 파일을 바로 부르는 방식)
