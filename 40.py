
digit_list = [int(digit) for number in range(1, 1000001) for digit in str(number)]
value = 1
value = int(digit_list[0])*int(digit_list[9])*int(digit_list[99])*int(digit_list[999])*int(digit_list[9999])*int(digit_list[99999])*int(digit_list[999999])
print(value)
