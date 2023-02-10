import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 가장 큰 값을 초기화, 0을 대비 하여 -1로 초기화 함
    max_num = -1

    # 이득본 금액
    price = 0

    # numbers 의 길이 만큼 반복
    for len_num in range(len(numbers)):

        # numbers 의 가장 뒤부터 탐색 하여 max_num 과 비교
        if max_num < numbers[-len_num-1]:
            max_num = numbers[-len_num-1]
        elif max_num > numbers[-len_num-1]:
            price += max_num - numbers[-len_num-1]

    print(f'#{tc} {price}')
