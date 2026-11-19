#计算1-100之间偶数的和
toko = 0
a = 1
while a  <= 100:
    if a % 2 == 0:
        toko += a
    a += 1
print(f'1-100之间的和是{toko}')
