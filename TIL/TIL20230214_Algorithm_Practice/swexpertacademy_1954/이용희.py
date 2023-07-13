import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0
    x = 0
    y = 0
    result = [[0 for col in range(N)] for row in range(N)]
    for step in range(1, N * N + 1):
        result[x][y] = step
        if idx == 0 and (y == N-1 or result[x][y+1]):
            idx += 1
        elif idx == 1 and (x == N-1 or result[x+1][y]):
            idx += 1
        elif idx == 2 and (y == 0 or result[x][y-1] != 0):
            idx += 1
        elif idx == 3 and (x == 0 or result[x-1][y] != 0):
            idx = 0
        x += dx[idx]
        y += dy[idx]

    print(f'#{test_case}')
    for i in range(N):
        print(*result[i])

