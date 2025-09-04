# 用户模块 API 文档

## 一、注册
- URL : `localhost:8000/user/register/`
- POST
- 参数 :
  1、username(string). 2、password(string)
- 返回：
```json
{
    "code" : 200 ,
    "message": "注册成功"
}
```

## 二、登录
- URL : `localhost:8000/user/login/`
- POST
- 参数:
  1、username(string). 2、password(string)
- 返回
```json
{ 
    "code": 200,
    "message": "登录成功"
}
```