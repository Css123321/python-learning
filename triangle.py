#验证三条边是否是等边，等腰，普通三角形
a = int(input("请输入a边长"))
b = int(input("请输入b边长"))
c = int(input("请输入c边长"))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print(f"{a} {b} {c}构成等边三角形")
    elif a == b or a == c or b == c:
        print(f"{a} {b} {c}构成等腰三角形")
    else:
        print(f"{a} {b} {c}构成普通三角形")    
else:
    print(f"{a} {b} {c}不构成三角形")