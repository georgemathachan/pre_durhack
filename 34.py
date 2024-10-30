def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

list1 = []

for i in range(10, 4000000):
    factorialsum = 0
    for digit in str(i):
        factorialsum += factorial(int(digit))  # Convert digit to int
    if factorialsum == i:
        list1.append(i)

print(list1)
