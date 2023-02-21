
def solution(input_string):
    answer = []
    string_dic = {}
    for string in input_string:
        string_dic[string] = []  # 입력 받은 문자를 키값으로 하는 딕셔너리 초기화

    string_num = 0
    for string in input_string:
        string_dic[string].append(string_num)  # 입력 받은 문자의 인덱스 값을 배열로 추가
        string_num += 1
    print(string_dic)
    string_set = 0
    for string_key in string_dic:  # 입력 받은 문자의 키값으로 순환
        for string_value in range(len(string_dic[string_key])):  # 각 키의 벨류값을 순환
            if string_value == 0:  # 처음 값이면
                string_set = string_dic[string_key][string_value]  # 변수에 저장
            else:  # 처음 값이 아니면
                if string_dic[string_key][string_value] - string_set != 1:  # 변수에 저장된 인덱스와 지금의 인덱스 차이가 1이 아닌게 있따면
                    answer.append(string_key)  # 결과 값에 키값을 저장
                string_set = string_dic[string_key][string_value]  # 인덱스값 갱신
    if len(string_dic) == 1:  # 입력 받은 문자가 1개라면
        for string_key in string_dic:
            answer.append(string_key)  # 결과 값에 저장

    done = ''
    for result in sorted(list(set(answer))):  # 결과값에 중복된 문자를 제거하고, 알파벳 순으로 정렬
        done += result  # 최종 결과 값에 더하기
    if not done:  # 만약 최종 결과 값이 없다면
        done = 'N'  # 최종 결과 값은 'N'
    print(done)


solution("eeddee")

