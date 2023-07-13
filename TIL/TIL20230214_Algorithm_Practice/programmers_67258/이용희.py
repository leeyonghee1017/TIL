gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems_type = list(set(gems))  # ["DIA", "RUBY", "EMERALD", "SAPPHIRE"]
#
# left = 0
# right = len(gems_type)
# answer = [0, 0]
#
# while True:
#     if list(set(gems[left:right])) != gems_type:
#         right += 1
#     else:
#         answer[1] = right
#         break
#
# while True:
#     if list(set(gems[left:right])) == gems_type:
#         left += 1
#     else:
#         answer[0] = left
#         break
# print(answer)

# O(n^2)
# def solution(gems):
#     N = minimum = len(gems)
#     uniq_count = len(set(gems))
#     answer = [1, N]
#     for start in range(0, N-uniq_count+1):
#         for end in range(start+uniq_count, N+1):
#             my_gems = gems[start:end]
#             if len(set(my_gems)) == uniq_count and len(my_gems) < minimum:
#                 minimum = len(my_gems)
#                 answer[0] = start + 1
#                 answer[1] = end
#                 break
#     return answer

start = 0
N = minimum = len(gems)
uniq_count = len(set(gems))
answer = [1, N]
gem_info = {}

for end in range(N):
    last_gems = gems[end]
    if gem_info.get(last_gems):
        gem_info[last_gems] += 1
    else:
        gem_info[last_gems] = 1

    while uniq_count == len(gem_info):
        count = end - start + 1
        if count < minimum:
            minimum = count
            answer = [start+1, end+1]
        first_gems = gems[start]
        gem_info[first_gems] -= 1
        if gem_info[first_gems] == 0:
            gem_info.pop(first_gems)
        start += 1

print(answer)
