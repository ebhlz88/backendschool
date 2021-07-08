"""backendschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from school import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.studentslist),
    path('student/<int:roll>', views.studentByroll),
    path('fees', views.feesget),
    path('feespost/<int:roll>/<int:yerr>/<str:month>/<str:standardd>',views.feespost),
    path('resultpost/<int:roll>/<int:yerr>/<str:standardd>/<str:ssubject>',views.postresult),
    path('yearlist', views.yearview),
    path('monthlist', views.monthsview),
    path('result/<int:sroll>', views.getstudentresult),

]
