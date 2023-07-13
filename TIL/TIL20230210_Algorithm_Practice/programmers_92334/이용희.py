def solution(id_list, report, k):
    report_count = dict()  # 신고된 횟수
    history = dict()  # 누가 누구를 신고했는지
    result = []
    list_num = 0
    for i in id_list:
        report_count[i] = 0
        history[i] = []
        result.append(0)
    check = 0
    for i in report:
        for x in history[i.split()[0]]:
            if x == i.split()[1]:
                check += 1
        if check == 0:
            history[i.split()[0]].append(i.split()[1])
            report_count[i.split()[1]] += 1
        check = 0

    for i in history:

        for x in history[i]:
            if report_count[x] >= k:
                result[list_num] += 1
        list_num += 1
    return result