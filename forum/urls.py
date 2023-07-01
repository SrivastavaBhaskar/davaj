from django.urls import path

from forum.views import (
    home_view,
    forum_home,
    create_thread,
    view_thread
)

urlpatterns = [
    path('', home_view, name='home'),
    path('forum/', forum_home, name='forum-home'),
    path('forum/create-thread', create_thread, name='create-thread'),
    path('forum/view-thread/<int:id>', view_thread, name='view-thread'),
]