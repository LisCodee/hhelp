# 数据字典

## 用户表(user)
|名称|类型|备注|
| ------ | ------ | ------ |
|id|int|主键、自增|
|email|varchar(30)|唯一，账号|
|password|varchar(20)|密码|
|isDoctor|0/1|0:是，1：否|
|lastlogin|Date()|最后登录时间|

## 忌吃清单(ban)
|名称|类型|备注|
| ------ | ------ | ------ |
|id|int|主键、自增|
|title|varchar(128)|病名，唯一|
|content|varchar(2*1024)|内容|

## 运动保健(sport)
|名称|类型|备注|
| ------ | ------ | ------ |
|id|int|主键、自增|
|title|varchar(128)|文章名称|
|content|varchar(3*1024)|文章内容|
|pub_user|int|关联自user_id,发布者id|
|pub_time|Date|发布时间|
|click_num|int|点击量|


# 接口

### 用户注册接口(/register)：
- 请求方式：POST
- 参数：
    * email
    * password
    * vercode(验证码)
- 返回值：
    * err_code
- 请求示例：
    * {email:'123456@qq.com',password:'1234',vercode:'1234'}
- 返回示例：
    * {err_code:0,err_msg:''}
    * 0:成功，1:该邮箱已被注册，2:验证码错误
    * 如果err_code为0，则err_msg返回空字符串

### 获取验证码接口(/getvercode):
- 请求方式：GET
- 参数：
    * email
- 返回值:
    * success/fail

### 用户登录接口(/login):
- 请求方式：POST
- 参数：
    * email
    * password
- 返回值：
    * err_code
    * err_msg
- 返回示例：
    * {err_code:1,err_msg:'用户名或密码错误'}

### 