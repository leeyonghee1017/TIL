N, M = map(int, input().split())
ant, aphid = [], []
for i in range(N):
    coor = list(map(int, input().split()))
    for j in range(N):
        if coor[j] == 1:
            ant.append([i,j])
        elif coor[j] == 2:
            aphid.append([i,j])
ans = len(ant)
for x1, y1 in ant:
    min_val = float('inf')
    for x2, y2 in aphid:
        dist = abs(x1 - x2) + abs(y1 - y2)
        min_val = min(min_val, dist)
    if min_val > M:
        ans -= 1

print(ans)