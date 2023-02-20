import sys
sys.stdin = open('input.txt')
T = int(input())


def dfs(idx, num, num_sum):
    if idx == len(numbers):
        if num == len(subset) and sum(subset) == num_sum:
            count[0] += 1
        return
    subset.append(numbers[idx])
    dfs(idx + 1, num, num_sum)
    subset.pop()
    dfs(idx + 1, num, num_sum)


for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    numbers = [i for i in range(1, 13)]
    subset = []
    count = [0]
    dfs(0, N, K)
    print(f'#{test_case} {count[0]}')
