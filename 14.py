# Create a list from 2 to 999998
list1 = list(range(2, 999999))
lengths = []

# Function to calculate the length of the Collatz sequence
def collatz_length(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Use integer division
        else:
            n = (3 * n) + 1
        count += 1
    return count

# Iterate over the list and calculate lengths
for number in list1:
    lengths.append(collatz_length(number))

# Find the maximum length and its corresponding index
max_length = 0
max_index = 0
for index in range(len(lengths)):
    if lengths[index] > max_length:
        max_length = lengths[index]
        max_index = index

# Print the number that has the longest Collatz sequence
print(list1[max_index])
