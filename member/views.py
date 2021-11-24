from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Member


# Create your views here.
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        r_password = request.POST.get('r_password')
        if password != r_password:
            return HttpResponse('两次输入的密码不同！')
        else:
            same_name_user = Member.objects.filter(username=username)
            if same_name_user:
                return HttpResponse('用户名已经存在！')
            same_email_user = Member.objects.filter(email=email)
            if same_email_user:
                return HttpResponse('该邮箱已经被注册了！')
        new_member = Member.objects.create_user(username=username, email=email, password=password)
        return HttpResponse('ok')


class LoginView(View):
    """用户登录"""

    def get(self, request):
        return render(request, 'login.html')
