#计算1-100之间偶数的和
#toko = 0
#while a  <= 100:
#    if a % 2 == 0:
#        toko += a
#   a += 1
#print(f'1-100之间的和是{toko}')


total = 0
for b in range(2, 101, 2):
    total += b
print(f"1-100 之间的偶数和是 {total}")