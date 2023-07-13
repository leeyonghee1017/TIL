import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        # 양방향 그래프 일 경우 아래 줄 추가
        # graph[end].append(start)
    S, G = map(int, input().split())

    def dfs():
        # DFS
        # 방문 여부
        visited = [False for _ in range(V + 1)]
        # 목적지
        to_visited = [S]
        while to_visited:
            # 현재 위치 = 목적지들에서 마지막
            current = to_visited.pop()
            # 현재 위치를 방문한 적이 없다면,
            if not visited[current]:
                # 현재 위치 방문 체크
                visited[current] = True
                # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
                to_visited += graph[current]

    def bfs():
        from collections import deque
        # 방문 여부
        visited = [False for _ in range(V + 1)]
        # 목적지
        to_visited = deque()
        to_visited.append(S)
        while to_visited:
            # 현재 위치 = 목적지들에서 마지막
            current = to_visited.popleft()
            # 현재 위치를 방문한 적이 없다면,
            if not visited[current]:
                # 현재 위치 방문 체크
                visited[current] = True
                # 현재 위치에서 갈 수 있는 정점들을 목적지들에 추가
                to_visited += graph[current]

