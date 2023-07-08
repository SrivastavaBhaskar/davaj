from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import EditProfileForm

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

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect(login_view)
    return render(request, 'accounts/logout.html')

def registration_view(request):
    form = UserCreationForm(data=request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect(login_view)
    return render(request, 'accounts/register.html', context=context)

@login_required
def user_profile_edit_view(request, username=None):
    if username == None:
        return redirect(forum_home)
    user = User.objects.get(username=username)
    form = EditProfileForm(data=request.POST or None)
    context = {
        'this_user': user,
        'form': form
    }
    if form.is_valid():
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        return redirect(user_profile_view, user.username)
    return render(request, 'accounts/profile.html', context=context)


def user_profile_view(request, username=None):
    if username == None:
        return redirect(forum_home)
    user = User.objects.get(username=username)
    context = {
        'this_user': user
    }
    return render(request, 'accounts/public-profile.html', context=context)
