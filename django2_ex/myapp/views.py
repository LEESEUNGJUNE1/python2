from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")
"""
print('GET 요청 처리')
    message = request.GET.get('message')
    gen = request.GET.get('gen')
    return render(request, 'show.html', {'message':message, 'gen':gen})
"""
def sendFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'show.html')

    elif request.method == 'POST':
        print('POST 요청 처리')
        message = request.POST.get('message')
        gen = request.POST.get('gen')
        return render(request,'show.html',{'message':message, 'gen':gen})

    else:
        print('요청 에러')
