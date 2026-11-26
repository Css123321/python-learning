scores = {"语文": 90, "数学": 85, "英语": 77}

# ① 打印语文成绩
print(scores["语文"])

# ② 加入 物理: 88
scores['物理'] = 88
print(scores["物理"])

# ③ 把数学改成 92
scores["数学"] = 92
print(scores["数学"])

# ④ 删除英语
del scores["英语"]

# ⑤ 打印整个字典
print(scores)

# ⑥ 用 get 查一个不存在的键 "化学"，默认显示 "没有这门课"
print(scores.get("化学", "没有这门课"))

# 算出总分
total = 0
for v in scores.values():
    total += v
print(total)

#输入：the cat and the dog
#输出：{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
text = input("请输入一句话: ")
words = text.split()       

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1   
print(count)