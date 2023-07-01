from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from forum.views import forum_home

# Create your views here.
def accounts_view(request):
    return redirect(login_view)

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect(forum_home)
    return render(request, 'accounts/login.html', context=context)

def registration_view(request):
    form = UserCreationForm(data=request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect(login_view)
    return render(request, 'accounts/register.html', context=context)