import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    now = []
    for end_point in range(100):
        if matrix[99][end_point] == 2:
            now = [98, end_point]

    while now[0] != 0:
        if now[1] == 99:
            if matrix[now[0]][now[1]-1] == 1:
                matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]
            else:
                now = [now[0]-1, now[1]]
        elif now[1] == 0:
            if matrix[now[0]][now[1]+1] == 1:
                matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] + 1]
            else:
                now = [now[0]-1, now[1]]
        else:
            if matrix[now[0]][now[1]-1] == 1:
                matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] - 1]
            elif matrix[now[0]][now[1]+1] == 1:
                matrix[now[0]][now[1]] = 0
                now = [now[0], now[1] + 1]
            else:
                now = [now[0] - 1, now[1]]

    print(f'#{test_case} {now[1]}')
