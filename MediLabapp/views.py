from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def starterpage(request):
    return render(request,'starterpage.html')

