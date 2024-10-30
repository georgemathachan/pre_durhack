def d(n):

    sum = 0

    for i in range(1, int(n/2) + 1):

            if n % i == 0:

                sum = sum + i

    if sum > n:

         abundant_numbers.add(n)

   

abundant_numbers = set([])

total = 0

for i in range(1, 28123):

     d(i)

 

numbers_that_can_be_made = set([])

 

for i in abundant_numbers:

    for j in abundant_numbers:

         numbers_that_can_be_made.add(i + j)

 

natural_numbers = set([])

 

for i in range(28123):

     natural_numbers.add(i)

 

new_list = natural_numbers - numbers_that_can_be_made

 

sum = 0

for i in new_list:

     if i < 28123:

          sum = sum + i

 

print(sum)