import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = input().split()
    puzzle = []
    # 단어의 길이
    word_len = int(N[1])
    # 퍼즐의 길이
    puzzle_len = int(N[0])
    # list 로 퍼즐 정보 저장
    for list_num in range(0, puzzle_len):
        puzzle.append(list(map(int, input().split())))

    # 퍼즐 안에 값이 0인지 1인지 확인 하는 변수
    zero_or_one_count = 0
    # zero_or_one_count 이 word_len 의 값과 같을때 카운팅 하는 변수
    search_word = 0
    # 퍼즐의 행 열 탐색(가로로 단어가 완성 되는 경우를 위해)
    for line in range(0, puzzle_len):
        for column in range(0, puzzle_len):
            # 퍼즐 안에 값이 1 이면
            if puzzle[line][column] == 1:
                zero_or_one_count += 1
            # 퍼즐 안에 값이 0 이면
            else:
                # zero_or_one_count 이 word_len 의 값과 같은지 확인
                if zero_or_one_count == word_len:
                    search_word += 1
                # 다시 zero_or_one_count 초기화
                zero_or_one_count = 0
        # 하나의 퍼즐의 열의 탐색이 끝나면 zero_or_one_count 와 word_len 가 같은지 확인
        if zero_or_one_count == word_len:
            search_word += 1
        zero_or_one_count = 0
    # 퍼즐의 열 행 탐색 (세로로 단어가 완성 되는 경우를 위해)
    for column in range(0, puzzle_len):
        for line in range(0, puzzle_len):
            if puzzle[line][column] == 1:
                zero_or_one_count += 1
            else:
                if zero_or_one_count == word_len:
                    search_word += 1
                zero_or_one_count = 0
        if zero_or_one_count == word_len:
            search_word += 1
        zero_or_one_count = 0

    print(f'#{test_case} {search_word}')


