from django.shortcuts import render

def community(request):
    return render(request,'community.html')

def create(request):
    return render(request,'create.html')

def detail(request):
    return render(request,'detail.html')
