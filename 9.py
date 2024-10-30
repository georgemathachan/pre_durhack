
list1 = []
for b in range(4, 501):
    for a in range(3, b):
        if (a**2 + b**2)**0.5 % 1 == 0:
            if a + b + (a**2 + b**2)**0.5 == 1000:
                print(a*b*((a**2 + b**2)**0.5))

