from collections import defaultdict

event, user = 4, 4

event_dic = defaultdict(int)
for _ in range(event):
    event_num = list(map(str, input().split()))
    for i in range(1, len(event_num)):
        event_dic[event_num[i]] += 1

result = [int(k) for k,v in event_dic.items() if max(event_dic.values()) == v]
result.sort(reverse=True)
result_str = ''
for i in range(len(result)):
    if i == len(result) - 1:
        result_str += str(result[i])
    else:
        result_str += str(result[i]) + ' '

print(result_str)