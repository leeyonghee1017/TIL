import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    h_buildings = list(map(int, input().split()))  # 빌딩의 높이 저장
    search = [-2, -1, 1, 2]  # 탐색할 인덱스값 저장
    count = 0
    for building_idx in range(len(h_buildings)):  # 빌딜 높이 리스트의 인덱스값 순환

        max_side = 0  # 주변 건물의 가장 높은 값을 저장할 변수 초기화
        if building_idx == 0 or building_idx == 1 or building_idx == N - 2 or building_idx == N - 1:
            continue  # 빌딩 높이 리스트의 인덱스가 0, 1, N-2, N-1이면 건너뛰기
        else:

            for search_num in search:
                if h_buildings[building_idx + search_num] > max_side:
                    max_side = h_buildings[building_idx + search_num]  # 주변 건물 중 가장 높은 건물 찾기
            if max_side < h_buildings[building_idx]:  # 주변 건물중 가장 높은 건물보다 지금 건물이 더 크면
                count += h_buildings[building_idx] - max_side  # 지금 건물 높이 - 주변 가장 높은 건물 높이의 값 저장
            else:
                continue
    print(f'#{test_case} {count}')
