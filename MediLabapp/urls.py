
from django.contrib import admin
from django.urls import path
from MediLabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,),
    path('starter-page',views.starterpage,),
]
