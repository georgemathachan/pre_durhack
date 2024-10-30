list = [1, 1]
while len(str(list[-1])) < 1000:
    list.append(int(list[len(list)-1])+int(list[len(list)-2]))
print(len(list))