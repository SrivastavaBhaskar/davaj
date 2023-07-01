from django.urls import path

from accounts.views import (
    accounts_view,
    login_view,
    registration_view
)

urlpatterns = [
    path('', accounts_view, name='accounts-home'),
    path('login/', login_view, name='accounts-login'),
    path('register/', registration_view, name='accounts-register')
]