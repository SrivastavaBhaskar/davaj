from django.urls import path

from accounts.views import (
    accounts_view,
    login_view,
    logout_view,
    registration_view,
    user_profile_view,
    user_profile_edit_view
)

urlpatterns = [
    path('', accounts_view, name='accounts-home'),
    path('login/', login_view, name='accounts-login'),
    path('logout/', logout_view, name='accounts-logout'),
    path('register/', registration_view, name='accounts-register'),
    path('<str:username>/edit/', user_profile_edit_view, name='edit-user-profile'),
    path('<str:username>/', user_profile_view, name='user-profile'),
]