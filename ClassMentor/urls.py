from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('', intro, name='intro'),
    path('fillform', fillform, name='form'),
    path('select', select, name='select'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('learn', learn, name='learn')
]
