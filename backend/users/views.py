from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

# 注册视图
@csrf_exempt
def register(request) :
    """
    GET : 返回注册界面
    POST ： 接受注册表单的数据，用来注册
    """
    if request.method != "POST" :
        return JsonResponse({'code': 405 , 'message' : 'Method Not Allowed'})
    
    # if request.method not in ["POST", "GET"]:
    #     return JsonResponse({'code': 405 , 'message' : 'Method Not Allowed'})

    data = json.loads(request.body) # 读取数据
    username = data.get('username' , '')
    password = data.get('password' , '')

    if User.objects.filter(username = username).exists() :
        return JsonResponse({'code': 200 , 'message': '用户已存在'})
    
    User.objects.create_user(username=username , password=password) # 创建用户
    return JsonResponse({'code':200 , 'message':'注册成功'})

# 登录视图
@csrf_exempt
def user_login(request) :
    """
    POST ： 接受登录表单的数据
    """
    if request.method != "POST" :
        return JsonResponse({'code':405 , 'message':'Method Not Allowed'})
    
    try :
        data = json.loads(request.body)
    except json.JSONDecodeError :
        return JsonResponse({'code':400 , 'message':'Invail Json'})

    username = data.get('username' , '')
    password = data.get('password' , '')
    user = authenticate(username = username , password = password)

    if user is not None :
        # 非空
        login(request , user)
        return JsonResponse({'code':200 , 'message':'登录成功'})
    else :
        return JsonResponse({'code':401 , 'message':'用户名或密码错误'})