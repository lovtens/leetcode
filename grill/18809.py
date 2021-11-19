import sys
from collections import deque
from itertools import combinations


def solution():
    n, m, g, r = map(int, sys.stdin.readline().strip().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().strip().split())))

    yellows = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                yellows.append((i, j))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def simulate(greens, reds):
        flower_count = 0
        green_q = deque(greens)
        red_q = deque(reds)
        visited = []
        for _ in range(n):
            visited.append([0] * m)

        for i, j in greens:
            visited[i][j] = 1
        for i, j in reds:
            visited[i][j] = 1
        while True:
            green_set = set()
            while green_q:
                # green
                x, y = green_q.popleft()
                for i in range(4):
                    try:
                        next_x = x + dx[i]
                        next_y = y + dy[i]
                        assert 0 <= next_x < n and 0 <= next_y < m
                        if board[next_x][next_y] != 0 and not visited[next_x][next_y]:
                            green_set.add((next_x, next_y))
                    except AssertionError:
                        pass
            red_set = set()
            while red_q:
                # red
                x, y = red_q.popleft()
                for i in range(4):
                    try:
                        next_x = x + dx[i]
                        next_y = y + dy[i]
                        assert 0 <= next_x < n and 0 <= next_y < m
                        if board[next_x][next_y] != 0 and not visited[next_x][next_y]:
                            red_set.add((next_x, next_y))
                    except AssertionError:
                        pass

            inter = green_set & red_set
            green_diff = green_set - inter
            red_diff = red_set - inter
            for i, j in inter:
                flower_count += 1
                visited[i][j] = 1
            for i, j in green_diff:
                green_q.append((i, j))
                visited[i][j] = 1
            for i, j in red_diff:
                red_q.append((i, j))
                visited[i][j] = 1
            if not green_q or not red_q:
                break
        return flower_count

    ret = 0

    for reds in combinations(yellows, r):
        for greens in combinations(filter(lambda x: x not in reds, yellows), g):
            result = simulate(list(greens), list(reds))
            ret = max(ret, result)
    print(ret)


solution()
