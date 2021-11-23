from django.db import models
# from django.contrib.auth.models import User
from member.models import Member


class DomainType(models.Model):
    type = models.CharField('域名类型', max_length=20)

    def __str__(self):
        return self.type


class RegisterPlatform(models.Model):
    platform = models.CharField('注册平台', max_length=150)

    def __str__(self):
        return self.platform


class Domain(models.Model):
    domain = models.CharField('域名', max_length=255)
    add_date = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    expired_date = models.DateTimeField(verbose_name='域名释放时间', blank=True, null=True)
    register_date = models.DateTimeField(verbose_name='域名注册时间', blank=True, null=True)

    domain_type = models.ForeignKey(DomainType, verbose_name='域名后缀', on_delete=models.PROTECT)
    register_platform = models.ManyToManyField(RegisterPlatform, verbose_name='注册平台')
    user = models.ManyToManyField(Member, verbose_name='域名归属')

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name = "域名"
        verbose_name_plural = verbose_name
