num = []
denom = []
expected = []
for i in range(11,100):
    for j in range(11, i):
        if i % 10 != 0 or j % 10 != 0:
            pass
        i_str = str(i)
        j_str = str(j)
        if i_str[0] == j_str[0] or i_str[1] == j_str[0] or i_str[0] == j_str[1] or i_str[1] == j_str[1]:
            num.append(j)
            denom.append(i)
            expected.append(j/i)

print(num)
print(denom)
print(expected)

