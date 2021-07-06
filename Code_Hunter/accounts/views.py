from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

def my_page(request):
    return render(request,'my_page.html')

def login_view(request):
    if request.method == 'POST':
        # post 형태의 request라면 login 하고 home으로
        form = AuthenticationForm(request= request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request= request, username = username, password = password)
            if user is not None:
                login(request, user)
            return redirect("/")
    else: 
        # post 형태의 request가 아니라면 login page를 보여준다.
        form = AuthenticationForm()
        return render(request,'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")


def signup(request):
    return render(request,'signup.html')