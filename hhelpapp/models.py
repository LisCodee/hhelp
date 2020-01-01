from django.db import models
from django.utils import timezone

# Create your models here.
# 用户表
class User(models.Model):
    id = models.AutoField(verbose_name="主键id，自增", primary_key=True)
    email = models.CharField(verbose_name="邮箱、账号", unique=True, max_length=32, null=False)
    password = models.CharField(verbose_name="密码，暂时不加密", max_length=32, null=True)
    is_doctor = models.IntegerField(verbose_name="是否专家，0是，1否", default=1)
    last_login = models.DateTimeField(verbose_name="最后登录时间", null=True)
    token = models.CharField(verbose_name="token", max_length=44, null=True)
    vercode = models.CharField(verbose_name="验证码", max_length=4, null=True)
    # doctype = models.CharField(vercode="主治类别", max_length=30, null=True)


# 忌吃清单
class ban(models.Model):
    id = models.AutoField(verbose_name="主键自增", primary_key=True)
    title = models.CharField(verbose_name="标题，病名", max_length=64, null=False)
    content = models.CharField(verbose_name="内容，标签内容", max_length=2048, null=False)


# 运动保健
class sport(models.Model):
    id = models.AutoField(verbose_name="主键自增", primary_key=True)
    title = models.CharField(verbose_name="文章标题", max_length=64, null=False)
    content = models.CharField(verbose_name="文章渲染后的内容", max_length=2048, null=False)
    pub_user = models.IntegerField(verbose_name="发表人id", null=False)
    pub_time = models.DateTimeField(verbose_name="发布时间", null=False)
    click_num = models.IntegerField(verbose_name="点击量", default=0, null=False)

