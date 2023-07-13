def solution(s, e):
    if s < e:
        count = (e - s) // 5
        s += count * 5
    elif s > e:
        return s - e

    # 목적지
    to_visits = [s]
    # 방문 여부
    visited = [False for _ in range(10001)]

    while to_visits:
        # 목적지 횟수 만큼 반복
        for _ in range(len(to_visits)):
            # 현재 위치 갱신
            current = to_visits.pop(0)
            # 방문한 적이 없다면
            if not visited[current]:
                # 방문 체크
                visited[current] = True
                # 찾았다면 끝
                if current == e:
                    return count
                # 못찾았다면 이동할 수 있는 선택지들
                for nxt in [current-1, current+1, current+5]:
                    # 선택지들이 범위 안이고, 방문한 적 없다면
                    if 0 < nxt <= 10000 and not visited[nxt]:
                        to_visits.append(nxt)
        count += 1
    return count


print(solution(5, 14))
print(solution(8, 3))
