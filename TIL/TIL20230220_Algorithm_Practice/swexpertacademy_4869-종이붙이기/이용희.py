import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int((int(input()))/10)
    paper = [0 for _ in range(31)]
    for paper_num in range(1, 31):
        if paper_num == 1:
            paper[paper_num] = 1
        elif paper_num == 2:
            paper[paper_num] = 3
        else:
            paper[paper_num] = paper[paper_num - 1] + (2 * paper[paper_num - 2])

    print(f'#{test_case} {paper[N]}')
