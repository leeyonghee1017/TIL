from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort(reverse=True)
    graph[end].sort(reverse=True)


def dfs():
    result = []
    dfs_visited = [False for _ in range(N + 1)]
    to_visited = [V]
    current = []

    while to_visited:
        current.append(to_visited.pop())
        if not dfs_visited[current[-1]]:
            dfs_visited[current[-1]] = True
            to_visited += graph[current[-1]]

    for current_num in range(len(current)):
        if current[current_num] not in result:
            result.append(current[current_num])
    return result

def bfs():
    # for i in range(len(graph)):
    #     graph[i].reverse()
    for graph_num in range(len(graph)):
        graph[graph_num].reverse()
    result = []
    bfs_visited = [False for _ in range(N + 1)]
    to_visited = deque()
    to_visited.append(V)
    current = []
    while to_visited:
        current.append(to_visited.popleft())
        if not bfs_visited[current[-1]]:
            bfs_visited[current[-1]] = True
            to_visited += graph[current[-1]]

    for current_num in range(len(current)):
        if current[current_num] not in result:
            result.append(current[current_num])
    return result


dfs_list = dfs()
bfs_list = bfs()

for dfs_list_num in dfs_list:
    print(dfs_list_num, end=' ')
print()
for bfs_list_num in bfs_list:
    print(bfs_list_num, end=' ')
