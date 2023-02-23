import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    containers_w = list(map(int, input().split()))
    trucks_t = list(map(int, input().split()))
    containers_w.sort(reverse=True)
    trucks_t.sort(reverse=True)
    total_w = 0
    for container in containers_w:
        for truck_idx in range(len(trucks_t)):
            if container <= trucks_t[truck_idx]:
                total_w += container
                trucks_t[truck_idx] = 0
                break
    print(f'#{test_case} {total_w}')
