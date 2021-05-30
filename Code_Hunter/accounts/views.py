from django.shortcuts import render

def my_page(request):
    return render(request,'my_page.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')