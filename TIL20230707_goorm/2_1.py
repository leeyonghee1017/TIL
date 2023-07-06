num1, num2, num3, num4 = map(int, input().split())
max_num = float("-inf")

if abs(num1-num2) + abs(num3-num4) > max_num:
	max_num = abs(num1-num2) + abs(num3-num4)
if abs(num1-num3) + abs(num2-num4) > max_num:
	max_num = abs(num1-num3) + abs(num2-num4)
if abs(num1-num4) + abs(num2-num3) > max_num:
	max_num = abs(num1-num4) + abs(num2-num3)

print(max_num)