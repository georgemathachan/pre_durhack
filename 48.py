num = 0
for i in range(1,1001):
    num += i**i
num = str(num)
print(str(num[-10])+str(num[-9])+str(num[-8])+str(num[-7])+str(num[-6])+str(num[-5])+str(num[-4])+str(num[-3])+str(num[-2])+str(num[-1]))