import random

answer = random.randint(1, 100)   # 随机生成 1-100 的答案
count = 0                         # 记录猜了几次

while True:
    guess = int(input("猜一个 1-100 的数字: "))
    count += 1                    # 每猜一次 +1

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print(f"猜对了！你一共猜了 {count} 次")
        break                     # 猜对就跳出循环
