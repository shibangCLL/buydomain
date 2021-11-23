from django.db import models
from django.contrib.auth.models import User


class Member(User):
    """自定义会员模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        verbose_name = '会员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
