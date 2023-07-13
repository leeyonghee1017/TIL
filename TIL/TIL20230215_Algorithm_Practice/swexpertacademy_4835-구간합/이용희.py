import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    X = list(map(int, input().split()))
    N = X[0]
    M = X[1]
    v = list(map(int, input().split()))
    max_value = 0
    min_value = 500000
    for v_idx in range(len(v)):
        v_sum = 0

        if v_idx != len(v) - M + 1:
            for M_idx in range(M):
                v_sum += v[v_idx + M_idx]

            if min_value > v_sum:
                min_value = v_sum
            if max_value < v_sum:
                max_value = v_sum
        else:
            break
    print(f'#{test_case} {max_value - min_value}')


