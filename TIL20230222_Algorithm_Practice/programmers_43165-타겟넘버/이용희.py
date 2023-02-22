from itertools import combinations


def solution(numbers, target):
    answer = 0
    idx_list = [idx for idx in range(len(numbers))]  # numbers의 인덱스를 저장하는 리스트 생성
    for idx in range(len(idx_list) + 1):  # combinations의 경우의 수를 전체까지 만들기 위해 +1
        for combinations_list in combinations(idx_list, idx):  # 인덱스 조합 생성
            sum_number = 0
            for number in range(len(numbers)):  # numbers 전체 순환
                cal = numbers[number]
                if number in combinations_list:  # 인덱스 조합에 있는 경우와 현재 인덱스 값이 같으면
                    cal *= -1  # 현재 인덱스 값의 숫자를 음수로 변환
                sum_number += cal  # 변수에 더하기
            if sum_number == target:  # 변수의 값과 target의 값이 같다면
                answer += 1  # 결과값 +1
    return answer


solution([4, 1, 2, 1], 4)
