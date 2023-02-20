import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    str_values = input()
    str_check = []
    result = 0

    for str_value in str_values:
        if str_value == '{':
            str_check.append(str_value)
        elif str_value == '(':
            str_check.append(str_value)
        if str_check:
            if str_value == ')' and str_check[-1] == '(':
                str_check.pop()
            elif str_value == ')' and str_check[-1] != '(':
                str_check.append(str_value)
                break
            elif str_value == '}' and str_check[-1] == '{':
                str_check.pop()
            elif str_value == '}' and str_check[-1] != '{':
                str_check.append(str_value)
                break
        else:
            if str_value == '}' or str_value == ')':
                str_check.append(str_value)
                break
    if str_check:
        result = 0
    else:
        result = 1

    print(f'#{test_case} {result}')
