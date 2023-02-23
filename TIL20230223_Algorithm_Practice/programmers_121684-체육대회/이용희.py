from itertools import permutations


def solution(ability):
    answer = 0
    for permutations_ability in permutations(ability, len(ability[0])):
        idx = 0
        sum_value = 0
        for per_ability in permutations_ability:
            sum_value += per_ability[idx]
            idx += 1
        if sum_value > answer:
            answer = sum_value
    return answer


solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
