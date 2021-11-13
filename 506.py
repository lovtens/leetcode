# https://leetcode.com/problems/relative-ranks/
# priority queue heap sorting
from queue import PriorityQueue
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        q = PriorityQueue()

        for i, v in enumerate(score):
            q.put((-v, i))

        answer = [''] * len(score)
        place = 1
        place_map = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }
        while not q.empty():
            v, i = q.get()
            answer[i] = place_map[place] if place <= 3 else str(place)
            place += 1

        return answer
