from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def account_base(request):
    return render(request, 'account_base.html')