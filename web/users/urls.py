from django.urls import path
from users.views import *


urlpatterns = [
    path('', Home.as_view()),
    path('login', Login.as_view()),
]
