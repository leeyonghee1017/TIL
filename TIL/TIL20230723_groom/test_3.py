N = int(input())

tile = []
for _ in range(N):
    tile.append(list(input()))

result = []
for i in range(N):
    result_str = ''
    for j in range(N):
        if tile[i][j] == '1':
            result_str += '0'
        else:
            min_value = float('inf')
            for n in range(i, N):
                if tile[n][j] == '1' and min_value > n - i:
                    min_value = n - i
            for n in range(j, N):
                if tile[i][n] == '1' and min_value > n - j:
                    min_value = n - j
            for n in range(i, -1, -1):
                if tile[n][j] == '1' and min_value > i - n:
                    min_value = i - n
            for n in range(j, -1, -1):
                if tile[i][n] == '1' and min_value > j - n:
                    min_value = j - n
            result_str += str(min_value)
    result.append(result_str)

for i in range(len(result)):
    result[i] = result[i].replace('inf','-1')

print(result)