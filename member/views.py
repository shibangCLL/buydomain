from django.shortcuts import render
from django.views import View


# Create your views here.
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        return render(request, 'registration.html')


class LoginView(View):
    """用户登录"""

    def get(self, request):
        return render(request, 'login.html')

