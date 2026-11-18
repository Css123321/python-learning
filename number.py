# 输入一个数，判断是正数、负数还是 0
num = int(input("输入一个数: "))

if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}是0")
