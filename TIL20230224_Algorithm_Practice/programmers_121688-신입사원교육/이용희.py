import heapq


def solution(ability, number):
    heapq.heapify(ability)
    print(ability)
    for _ in range(number):
        p1 = heapq.heappop(ability)
        p2 = heapq.heappop(ability)
        p3 = p1 + p2
        heapq.heappush(ability, p3)
        heapq.heappush(ability, p3)

    print(sum(ability))
    # answer = 0
    # for num in range(number):
    #     ability.sort()
    #     sum_ability = ability[0] + ability[1]
    #     ability[0] = sum_ability
    #     ability[1] = sum_ability
    # for ability_num in ability:
    #     answer += ability_num
    # print(answer)


solution([10, 3, 7, 2], 2)
