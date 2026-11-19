#实现简易计算器
num1 = float(input('请输入第一个数'))
num2 = float(input('请输入第二个数'))
CS = input("请输入运算符号(+ — * /) : ")
match CS:
    case "+" :
        print(f"{num1} + {num2} = { num1 + num2 }")
    case "-" :
        print(f"{num1} - {num2} = { num1 - num2 }")
    case "*" :
        print(f"{num1} * {num2} = { num1 * num2 }")
    case "/" :
        print(f"{num1} / {num2} = { num1 / num2 }")
    case _ :
        print("操作不支持")