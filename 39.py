ps = []
for i in range(4, 501):
    for j in range(3, i + 1):
        hypotenuse = (i**2 + j**2)**0.5
        if hypotenuse.is_integer(): 
            perimeter = i + j + int(hypotenuse)  
            if perimeter < 1001:
                ps.append(perimeter)
counts = {}
for item in ps:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
most_common_element = None
most_common_count = 0
for item, count in counts.items():
    if count > most_common_count:
        most_common_count = count 
        most_common_element = item
print(most_common_element)
print(most_common_count)