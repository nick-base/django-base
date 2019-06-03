from django.views import View
from django.http import HttpResponse
from utils.http import response_success

class Home(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, home page!')

class Login(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        password = request.POST.get('password', '')
        return response_success({'name': name})
