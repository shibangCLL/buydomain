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


class RegisterPlatform(models.Model):
    platform = models.CharField('注册平台', max_length=150)

    def __str__(self):
        return self.platform


class Godaddy(models.Model):
    """Godaddy Api,用于查询域名是否可以注册"""
    api_key = models.CharField(max_length=250, verbose_name='api_key')
    api_secret = models.CharField(max_length=250, verbose_name='api_secret')
    add_date = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    user = models.ForeignKey(Member, verbose_name='api归属', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Godaddy账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class Versio(models.Model):
    """Versio账户信息，用于注册0.99nl be"""
    username = models.CharField(max_length=250, verbose_name='账户用户名')
    password = models.CharField(max_length=250, verbose_name='账户密码')
    nl_contact_id = models.CharField(max_length=6, verbose_name='nl联系人id')
    be_contact_id = models.CharField(max_length=6, verbose_name='be联系人id')
    add_date = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    user = models.ForeignKey(Member, verbose_name='Versio归属', on_delete=models.PROTECT)
    register_platform = models.ManyToManyField(RegisterPlatform, verbose_name='注册平台')

    class Meta:
        verbose_name = 'Versio账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class AfterMarket(models.Model):
    """AfterMarket账户信息，用于注册pl域名"""
    api_key = models.CharField(max_length=250, verbose_name='api_key')
    api_secret = models.CharField(max_length=250, verbose_name='api_secret')
    add_date = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    user = models.ForeignKey(Member, verbose_name='api归属', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'AfterMarket账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class Openprovider(models.Model):
    """Openprovider账户信息，用于注册fr es it de等域名"""
    username = models.CharField(max_length=250, verbose_name='账户用户名')
    password = models.CharField(max_length=250, verbose_name='账户密码')
    nl_contact_id = models.CharField(max_length=20, verbose_name='nl联系人id')
    be_contact_id = models.CharField(max_length=20, verbose_name='be联系人id')
    es_contact_id = models.CharField(max_length=20, verbose_name='es联系人id')
    fr_contact_id = models.CharField(max_length=20, verbose_name='fr联系人id')
    ch_contact_id = models.CharField(max_length=20, verbose_name='ch联系人id')
    de_contact_id = models.CharField(max_length=20, verbose_name='de联系人id')
    eu_contact_id = models.CharField(max_length=20, verbose_name='eu联系人id')
    it_contact_id = models.CharField(max_length=20, verbose_name='it联系人id')
    add_date = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)
    user = models.ForeignKey(Member, verbose_name='Openprovider归属', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Openprovider账户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user
