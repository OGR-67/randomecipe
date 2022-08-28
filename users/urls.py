from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('user-account/', views.user_account, name='user_account'),
    path('user-account/del/', views.del_account, name='del_account'),
]
