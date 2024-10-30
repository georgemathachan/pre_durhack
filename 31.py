number = 8

for a in range(0, 200):
    for b in range(0, 100):
        for c in range(0, 40):
            for d in range(0, 20):
                for e in range(0, 10):
                    for f in range(0, 4):
                        for g in range(0, 2):
                            if a+b+c+d+e+f+g == 200:
                                number += 1

print(number)
