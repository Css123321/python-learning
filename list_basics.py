s = ['a', 'z', 'x', 'c', 'v', 'b']
print(s[0])# a   ← 索引从 0 开始
print(s[-1])  # b  ← 最后一个
print(s[0:-1])  #  ← 切片：含头不含尾
print(s[2]) # x
s.append("n") # 末尾加一个
s.insert(1,"m")    # 索引 1 处插入
s.remove("x")      # 删除值为 x 的
s.pop(-1)          # 删最后一个