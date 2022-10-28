from django.contrib import admin
from django.urls import path

from task.views import  home,vote,next,previous,start

urlpatterns = [
    path('admin/', admin.site.urls),
    path('next/',next,name='next'),
    path('previous/',previous,name='previous'),
    path('h/<str:pk>',vote),
    path('home/',home,name='home'),
    path('',start,name='hello'),

    
]