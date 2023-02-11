from django.urls import path, include
from users.views import login_view, signup_view, home_view, error_page, logout_view
from todo.urls import *
from todo.views import *

urlpatterns = [ 
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('tasks/', TaskList.as_view(), name = 'tasks'),
    path('error/', error_page, name='404'),
    path("todo/", include("todo.urls")),
    path("logout/", logout_view, name='logout'),
]

