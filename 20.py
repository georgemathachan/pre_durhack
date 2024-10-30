def solution_procedural() -> int:
    factorial = 1
    for factor in range(1,101):
        factorial *= factor
    
    digit_sum = 0
    for digit_char in str(factorial):
        digit_sum += int(digit_char)

    return digit_sum

print(solution_procedural())    



    