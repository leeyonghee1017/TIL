number = input().split()
results = []

for num in number:
	result = eval(num)
	results.append(result)
	
max_value = max(results)
print(max_value)

# ex)
# input : 
#   10*10-99 99-10*10
# output : 
#   1