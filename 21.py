def d(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
    return sum 

total = 0

for i in range(1, 10001):
    x = d(i)
    if i == d(d(i)) and i != d(i):
        total = total + i

print(total)