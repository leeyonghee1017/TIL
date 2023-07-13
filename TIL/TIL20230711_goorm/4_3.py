from itertools import permutations

input_count = int(input())

input_num = list(map(int, input().split()))
min_val = float('inf')

for i in permutations(input_num, input_count):
    val = i[0]
    for j in range(1, input_count):
        if val % 10 == i[j] // 10:
            val = val * 10 + i[j] % 10
        else:
            val = val * 100 + i[j]
    min_val = min(min_val, val)

print(min_val)