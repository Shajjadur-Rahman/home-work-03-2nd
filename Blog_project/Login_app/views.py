from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm


@unauthenticated_user
def sign_up_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Login_app:login'))

    context = {
        'form': form
    }
    return render(request, 'account/signUp.html', context)


@unauthenticated_user
def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Blog_app:home'))

    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)



@login_required
def log_out_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:login'))

@login_required
def user_profile(request):
    return render(request, 'account/profile.html')

@login_required
def edit_user_profile(request):
    return render(request, 'account/edit_profile.html')

@login_required
def change_pro_pic(request):

    return render(request, 'account/change_pro_pic.html')