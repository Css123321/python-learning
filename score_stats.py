#请同学输入共 5 个成绩,有总分,平均分,最高分,最低分
num_list = []
for i in range(5):
    num = int(input("请输入有效数字"))
    num_list.append(num)
print(sum(num_list)) #总分

num_list.sort()#排序
print(num_list[-1]) #最大数
print(num_list[0]) #最小数

print(sum(num_list)/len(num_list))  #平均数
