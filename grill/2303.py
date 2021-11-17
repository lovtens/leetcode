import sys
from typing import List


def solution():
    n = int(sys.stdin.readline().strip())
    card_list = []
    for _ in range(n):
        card_list.append(list(map(int, sys.stdin.readline().strip().split())))

    def get_max_value(cards: List[int]):
        total_sum = sum(cards)
        ret = -1
        for i in range(len(cards)):
            for j in range(len(cards)):
                if i == j:
                    continue
                ret = max(ret, (total_sum - cards[i] - cards[j]) % 10)
        return ret

    max_idx = n - 1
    max_value = -1
    for i in range(n):
        v = get_max_value(card_list[i])
        if max_value <= v:
            max_value = v
            max_idx = i

    print(max_idx+1)

solution()



