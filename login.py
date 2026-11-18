# 正确的账号密码（用字符串存）
ok_A = "1234"
ok_B = "4321"

# 接收用户输入（input 返回的是字符串）
A = input("请输入账号: ")
B = input("请输入密码: ")

# 账号和密码都正确，才能进入
if A == ok_A and B == ok_B:
    print("欢迎")
else:
    print("账号或者密码错误")
