# main urls.py로 부터 위임받은 urls
from django.urls import path
from myapp import views

urlpatterns = [
    path('show', views.sendFunc),
    #path('insertok', views.insertokFunc), 
    ]