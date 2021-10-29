# https://leetcode.com/problems/rotting-oranges/
# bfs queue matrix
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx_list = [0, 0, 1, -1]
        dy_list = [1, -1, 0, 0]

        def count_fresh_orange():
            fresh_orange_count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        fresh_orange_count += 1
            return fresh_orange_count

        max_depth = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    # i, j, depth
                    grid[i][j] = 2
                    q.append((i, j, 0, [(i, j)]))

        while len(q) > 0:
            x, y, depth, stack = q.popleft()
            # print(x,y, depth, stack)
            max_depth = max(max_depth, depth)
            for i in range(len(dx_list)):
                dx = dx_list[i]
                dy = dy_list[i]
                try:
                    assert (dx + x in range(len(grid)) and dy + y in range(len(grid[0])))
                    target = grid[dx + x][dy + y]
                    if target == 1:
                        # print('rotting', dx+x, "", dy+y)
                        grid[dx + x][dy + y] = 2
                        q.append((dx + x, dy + y, depth + 1, stack + [(dx + x, dy + y)]))
                    elif target == 0:
                        grid[dx + x][dy + y] = -1  # visited
                    elif target == -1:
                        # visited
                        pass
                except AssertionError as e:
                    continue

        # print(grid)
        if count_fresh_orange() == 0:
            return max_depth
        else:
            return -1


# 2 1 1 1 1
# 0 1 1 1 2
# 0 0 1 1 2

