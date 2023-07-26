import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())

# 디폴트 딕셔너리 선언
graph = defaultdict(list)

# 데이터 입력
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


# BFS 큐로 구현. deque 자료형 사용
Q = deque()
Q.append(1)
visited = [10e9 for _ in range(N+1)]
visited[1] = 0