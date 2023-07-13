import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    matrix = [[0 for _ in range(100)] for _ in range(100)]  # row, column 각각 100인 메트릭스 0으로 초기화
    max_sum = 0  # 결과값을 저장할 변수
    for row in range(100):
        matrix[row] = list(map(int, input().split()))  # 값 입력
    for row in range(100):  # row 탐색
        if max_sum < sum(matrix[row]):
            max_sum = sum(matrix[row])  # row의 총합이 max_sum보다 크다면 max_sum 갱신
    for column in range(100):  # column 탐색
        sum_value = 0  # 탐색한 총 합 초기화
        for row in range(100):
            sum_value += matrix[row][column]  # 탐색한 값을 더하기
        if max_sum < sum_value:
            max_sum = sum_value  # column의 총합이 max_sum보다 크다면 max_sum 갱신

    sum_cross_value = 0
    for cross in range(100):  # 좌상에서 우하로 내려가는 대각선 탐색
        sum_cross_value += matrix[cross][cross]  # 탐색한 값을 더하기
    if max_sum < sum_cross_value:
        max_sum = sum_cross_value  # 대각선의 총합이 max_sum보다 크다면 max_sum 갱신

    sum_reverse_cross_value = 0
    for cross in range(99, -1, -1):  # 우상에서 좌하로 내려가는 대각선 탐색
        sum_reverse_cross_value += matrix[cross][cross]  # 탐색한 값을 더하기
    if max_sum < sum_reverse_cross_value:
        max_sum = sum_reverse_cross_value  # 대각선의 총합이 max_sum보다 크다면 max_sum 갱신

    print(f'#{test_case} {max_sum}')
