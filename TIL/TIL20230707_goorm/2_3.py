import math

input_count = int(input())
num = list(map(int, input().split()))
total_num = 0
for num_idx in range(len(num)):
	check_num = 0
	prime_num = num_idx + 1	
	if prime_num > 1:
		for i in range(2, int(math.sqrt(prime_num) + 1)):
			if check_num != 0:
				break
			if prime_num % i == 0:
				check_num = 1
		if check_num == 0:
			total_num += num[num_idx]
print(total_num)