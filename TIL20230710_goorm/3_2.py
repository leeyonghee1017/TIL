answer = [int(i) for i in input()]
input_num = [int(i) for i in input()]

count = 0
while True:
    count += 1
    result = [2, 2, 2, 2]
    if input_num == answer:
        print(count)
        break

    for i in range(4):      
        if input_num[i] in answer:
            if input_num[i] == answer[i]:
                result[i] = 0
            else:
                result[i] = 1
    
    for i in range(4):
        if result[i] != 2:
            continue
        while True:
            cal_num = (input_num[i] + 1) % 10
            cal_check = cal_num not in input_num
            input_num[i] = cal_num
            if cal_check:
                break
    
    if 1 in result:
        pos = []
        value = []
        for i in range(4):
            if result[i] != 0:
                pos.append(i)
                value.append(input_num[i])
        for i in range(len(pos)):
            if i == 0:
                input_num[pos[i]] = value[-1]
            else:
                input_num[pos[i]] = value [i - 1]