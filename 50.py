import math
maxnumber = 1000000
numbers = list(range(2, maxnumber + 1))
primes = []
for i in numbers:
    prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if (i % j) == 0:
            prime = False
            break
    if prime:
        primes.append(i)
        multiples = [k for k in range(2 * i, maxnumber + 1, i)]
        numbers = [num for num in numbers if num not in multiples]

sum = 0
for i in range(1,78000):
   for j in primes:
       sum += j

