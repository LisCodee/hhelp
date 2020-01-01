from django.http import JsonResponse, HttpResponse
from hhelpapp import models
from . import util
import time
import json
from django.core import serializers

"""
用户注册接口：
    1.获取邮箱，密码，验证码
    2.插入数据库
    3.返回值
"""


def register(request):
    response = {}
    if request.method == "POST":
        print(request.body)
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        vercode = body['vercode']
        user = models.User.objects.filter(email=email, vercode=vercode).first()
        if user is None:
            response['err_code'] = 4
            response['err_msg'] = "未知错误"
        else :
            user.password = password
            user.vercode = ''
            user.save()
            response['err_code'] = 0
            response['err_msg'] = ""
    return JsonResponse(data=response)


"""
获取验证码接口
"""


def getvercode(request):
    response = {}
    # print(request.method)
    if request.method == "GET":
        email = request.GET.get("email")
        user = models.User.objects.filter(email=email).first()
        print(user)
        if user is None:
            vercode = util.createvercode()
            # print(vercode)
            if util.send_email(email, vercode) == 0:
                models.User.objects.create(email=email, vercode=vercode)
                response['err_code'] = 0
                response['err_msg'] = ''
                response['vercode'] = vercode
            else:
                response['err_code'] = 4
                response['err_msg'] = '未知错误'
        else:
            response['err_code'] = 1
            response['err_msg'] = '邮箱已被注册'
    return JsonResponse(data=response)


"""
用户登录接口
"""


def login(request):
    response = {}
    if request.method == "POST":
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        user = models.User.objects.filter(email=email).first()
        if user is not None:
            if password == user.password:
                token = util.createtoken(user.email)
                user.last_login = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                user.token = token
                user.save()
                response['err_code'] = 0
                response['err_msg'] = ''
                response['token'] = token
            else:
                response['err_code'] = 3
                response['err_msg'] = '用户名或密码错误'
        else:
            response['err_code'] = 5
            response['err_msg'] = '用户不存在'
    return JsonResponse(data=response)


"""
判断邮箱是否被注册
"""


def is_register(request):
    response = {}
    if request.method == "GET":
        email = request.GET.get('email')
        user = models.User.objects.filter(email=email).first()
        if user is None:
            response['err_code'] = 0
            response['err_msg'] = ''
        else:
            response['err_code'] = 1
            response['err_msg'] = '邮箱已被注册'
    return JsonResponse(data=response)


"""
测试接口
"""


def test(request):
    return JsonResponse({'status':'ok'})


"""
获取忌吃清单列表
"""


def getBanList(request):
    response = {}
    if request.method == "GET":
        token = request.GET.get("token")
        user = models.User.objects.filter(token=token)
        if user is None:
            response['err_code'] = 3
            response['err_msg'] = '用户名或密码错误'
            return JsonResponse(data=response)
        else:
            banList = models.ban.objects.filter()
            banList = serializers.serialize("json", banList)
            response['err_code'] = 0
            response['err_msg'] = ''
            response['data'] = banList
    return JsonResponse(data=response)


"""
获取保健内容
"""


def getSportList(request):
    response = {}
    if request.method == "GET":
        token = request.GET.get("token")
        user = models.User.objects.filter(token=token)
        if user is None:
            response['err_code'] = 3
            response['err_msg'] = '用户名或密码错误'
            return JsonResponse(data=response)
        else:
            sportList = models.sport.objects.filter()
            sportList = serializers.serialize("json", sportList)
            response['err_code'] = 0
            response['err_msg'] = ''
            response['data'] = sportList
    return JsonResponse(data=response)


"""
获取专家列表
"""


def getDoctorList(request):
    response = {}
    if request.method == "GET":
        token = request.GET.get("token")
        user = models.User.objects.filter(token=token)
        if user is None:
            response['err_code'] = 3
            response['err_msg'] = '用户名或密码错误'
            return JsonResponse(data=response)
        else:
            doctorList = models.User.objects.filter(is_doctor=0)
            doctorList = serializers.serialize()
            response['err_code'] = 0
            response['err_msg'] = ''
            response['data'] = doctorList
    return JsonResponse(data=response)