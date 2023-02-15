import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = input()
    nums_list = []
    nums_dic = {}
    result = [0, 0]
    for num in nums:
        nums_list.append(num)

    nums_list = set(nums_list)

    for num in nums_list:
        nums_dic[num] = 0

    for num in nums:
        nums_dic[num] += 1

    for nums_dic_key in nums_dic.keys():
        if nums_dic[nums_dic_key] > result[1]:
            result[1] = nums_dic[nums_dic_key]
            result[0] = int(nums_dic_key)
        elif nums_dic[nums_dic_key] == result[1] and result[0] < int(nums_dic_key):
            result[0] = int(nums_dic_key)

    print(f'#{test_case} {result[0]} {result[1]}')
