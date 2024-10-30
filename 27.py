a = int()
b = int()
n = 0
y = n**2 + a*n + b
count = 0
count_max = 0
def is_prime(y):
    if y <= 1:
        return False
    for i in range(2, int(y**0.5) + 1):
        if y % i == 0:
            return False
    return True

for i in range(-999, 1000):
    for j in range(-1000, 1001):
        n = 0
        count = 0
        while True:
            y = n**2 + i*n + j 
            if is_prime(y):
                n += 1
                count += 1
            else:
                break
        if count > count_max:
            count_max = count
            a = i
            b = j


print(a)
print(b)
print(count_max)
