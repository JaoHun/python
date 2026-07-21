"""
age=18
if age >= 18:
    print("你已成年")
else:   # 注意 else 不可以缩进，应该和 if 对齐
    print("你未成年")

score=100
if score >= 90:
    print("成绩优秀")
elif score >= 60:
    print("成绩合格")
else:
    print("成绩不合格")

userName = input("请输入用户名：")
userPassword = input("请输入用户密码：")

if userName == "MJH":
    if userPassword == "123456":
        print("登陆成功")
    else:
        print("登陆失败")
else:
    print("用户名或密码错误")
"""

answer = int(input("请输入一个数："))
if answer ==  8:
    print("猜对了")
elif answer >= 8:
    print("猜大了")
else:
    print("猜小了")

