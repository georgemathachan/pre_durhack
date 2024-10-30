list1 = []
for i in range(2, 101):
    for j in range(2, 101):
        list1.append(int(i**j))
seta = set(list1)
print(len(seta))