# https://leetcode.com/problems/task-scheduler/submissions/
# greedy heap priority queue

from collections import Counter, deque
from queue import PriorityQueue
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = Counter(tasks)
        pq = PriorityQueue()
        cooling = deque()
        # result = []
        i = 0
        for k, v in counter.items():
            pq.put((-v, -3, k))
        while not pq.empty() or len(cooling) > 0:
            if pq.empty():
                i = cooling[0][1] + n + 1

            while len(cooling) > 0 and cooling[0][1] + n < i:
                pq.put(cooling.popleft())

            v, recent, k = pq.get()
            # result.append(k)
            if v + 1 < 0:
                # n > 0이니까 무조건 쿨링으로
                cooling.append((v + 1, i, k))
            i += 1

        # print(result)
        return i


tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
result = Solution().leastInterval(tasks, n)
