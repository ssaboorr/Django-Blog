from django.shortcuts import render, HttpResponseRedirect
from .forms import Register, LoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import BlogPost


# Create your views here.

def home(request):
    posts = BlogPost.objects.all()

    return render(request, 'post/home.html',{'posts':posts})


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':

            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
    else:
        return HttpResponseRedirect('/dashboard/')

    return render(request, 'post/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def dashboard(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all()

        return render(request, 'post/dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')


def user_register(request):
    if request.method == 'POST':

        form = Register(request.POST)
        if form.is_valid():
            messages.success(request, 'Your Registration is Successful!! You can now Log in ')
            form.save()
    else:
        form = Register()

    return render(request, 'post/signup.html', {'form': form})
