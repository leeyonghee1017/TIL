import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    schedules = [list(map(int, input().split())) for _ in range(N)]
    schedules.sort(key=lambda x: (x[1], x[0]))
    answer = 0
    last = 0
    for s, e in schedules:
        if s >= last:
            answer += 1
            last = e

    print(f'#{test_case}', answer)
