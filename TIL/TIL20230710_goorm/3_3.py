boom_map_idx, boom_count = map(int, input().split())
boom_map = [[0 for i in range(boom_map_idx + 2)] for i in range(boom_map_idx + 2)]

for i in range(boom_count):
    input_coor = list(map(int, input().split()))
    boom_map[input_coor[0]][input_coor[1]] += 1
    boom_map[input_coor[0] + 1][input_coor[1]] += 1
    boom_map[input_coor[0]][input_coor[1] + 1] += 1
    boom_map[input_coor[0] - 1][input_coor[1]] += 1
    boom_map[input_coor[0]][input_coor[1] - 1] += 1
		
result = 0
for i in range(1, boom_map_idx + 1):
    for j in range(1, boom_map_idx + 1):
        result += boom_map[i][j]
      
print(result)