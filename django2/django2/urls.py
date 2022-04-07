"""django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gtapp import views
from gtapp.views import CallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.mainFunc), # Function views 요청이 들어오면 함수를 부른다. - 권장X (하나씩 부르는건 ㄱㅊ)
    path('abc/callget', CallView.as_view()), #Class-based views
    path('member/', include('gtapp.urls')) # gtapp에 있는 모든 member를 관리,위임 Including another URLconf
]
