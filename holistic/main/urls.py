from django.urls import path
from .views import index, register, user_login, special, user_logout

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('special/', special, name='special'),
]
