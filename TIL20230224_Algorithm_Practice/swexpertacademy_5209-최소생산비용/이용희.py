# from itertools import permutations
import sys
sys.stdin = open('input.txt')


def backtrack(product_idx, sum_cost):
    global minimum_cost
    if product_idx == N:
        if sum_cost < minimum_cost:
            minimum_cost = sum_cost
        return

    for factory_idx in range(N):
        if not visited[factory_idx]:
            visited[factory_idx] = True
            new_sum_cost = sum_cost + cost[product_idx][factory_idx]
            if new_sum_cost < minimum_cost:
                backtrack(product_idx + 1, new_sum_cost)
            visited[factory_idx] = False


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    minimum_cost = float('inf')
    visited = [False for _ in range(N)]
    backtrack(0, 0)
    print(f'#{test_case} {minimum_cost}')

# for test_case in range(1, T + 1):
#     N = int(input())
#     cost = [list(map(int, input().split())) for _ in range(N)]
#     minimum_cost = float('inf')
#     for permutations_idx in permutations(range(N)):
#         sum_cost = 0
#         for factory_idx, product_idx in enumerate(permutations_idx):
#             sum_cost += cost[product_idx][factory_idx]
#             if sum_cost >= minimum_cost:
#                 break
#         if sum_cost < minimum_cost:
#             minimum_cost = sum_cost
#     print(f'#{test_case} {minimum_cost}')
