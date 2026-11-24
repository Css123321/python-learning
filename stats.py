scores = [90, 85, 77, 92, 60]

# ① 用 for 遍历打印每个分数
for i in scores:
    print(i)

# ② 自己写循环算总分（不准用 sum）
total = 0
for i in scores:
    total += i
print(total)    
# ③ 用内置函数验证
print(sum(scores))    # 404   求和
print(max(scores))    # 92    最大值
print(min(scores))    # 60    最小值
print(len(scores))    # 5     个数
