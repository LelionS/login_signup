# accounts/urls.py

from django.urls import path
from .views import login_signup

urlpatterns = [
    path('', login_signup, name='login_signup'),
]
