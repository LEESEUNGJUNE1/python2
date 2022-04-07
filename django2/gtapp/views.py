from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "index.html")

class CallView(TemplateView):
    template_name = "callget.html"

"""
def insertFunc(request):
    return render(request, 'insert.html')

def insertokFunc(request):
    #irum = request.GET.get('name')
    irum = request.GET['name']
    print(irum)
    return render(request,'list.html',{'irum':irum})
"""

def insertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        return render(request, 'insert.html') # forward 방식
    
    elif request.method == 'POST':
        print('POST 요청 처리')
        irum = request.POST.get('name')
        return render(request,'list.html',{'irum':irum})
    
    else:
        print('요청 에러')