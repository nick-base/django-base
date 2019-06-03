from django.urls import path
from users.views import *


user_urls = [
    path('', Home.as_view()),
]
