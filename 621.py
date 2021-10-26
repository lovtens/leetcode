from collections import Counter
from queue import PriorityQueue
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        recent = {key: -n - 1 for key in counter.keys()}
        pq = PriorityQueue()
        for k, v in counter.items():
            pq.put((-v, k))

        i = 0
        tmp = PriorityQueue()
        while True:
            # print('tmp', tmp.queue)
            # print('pq', pq.queue)
            # print('result', result)
            # print('----')
            if pq.empty():
                if tmp.empty():
                    break
                while True:
                    if tmp.empty():
                        break
                    a = tmp.get()
                    r, pair = a
                    if r + n < i + 1:
                        pq.put(pair)
                    else:
                        tmp.put((r, pair))
                        break
                i += 1
                # result.append('idle')
            else:
                pair = pq.get()
                v, k = pair
                if i <= recent[k] + n:
                    tmp.put((recent[k], pair))
                else:
                    recent[k] = i
                    i += 1
                    # result.append(k)
                    if -v - 1 > 0:
                        pq.put((v + 1, k))
                    while True:
                        if tmp.empty():
                            break
                        r, pair = tmp.get()
                        if r + n < i:
                            pq.put(pair)
                        else:
                            tmp.put((r, pair))
                            break
        # print(result)
        return i


result = Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
print(result)