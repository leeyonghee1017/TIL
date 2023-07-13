import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    str_values = input()
    str_check = []
    result = 0
    for str_value in str_values:
        if str_check:
            if str_check[-1] == str_value:
                del str_check[-1]
            else:
                str_check.append(str_value)
        else:
            str_check.append(str_value)
    for _ in range(len(str_check)):
        result += 1

    print(f'#{test_case} {result}')
