input_count = int(input())
num = list(map(int, input().split()))
total_num = 0
for num_idx in range(len(num)):
	total_num += num[num_idx]
	
print(format(total_num, 'o'))