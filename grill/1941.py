import sys
from collections import deque

ret = 0


def solution():
    n = 5
    board = []
    selected = []
    for _ in range(n):
        board.append(list(sys.stdin.readline().strip()))
        selected.append([0] * 5)

    def get_next_position(x: int, y: int):
        if y == n - 1:
            return x + 1, 0
        else:
            return x, y + 1

    def prev_position(x: int, y: int):
        if y == 0:
            return x - 1, n - 1
        else:
            return x, y - 1

    def is_connected(x: int, y: int):
        visited = []
        for _ in range(n):
            visited.append([0] * n)

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque([[x, y]])
        visited[x][y] = 1
        count = 1

        while q:
            cur = q.popleft()
            for i in range(4):
                try:
                    next_x = cur[0] + dx[i]
                    next_y = cur[1] + dy[i]
                    assert 0 <= next_x < n and 0 <= next_y < n

                    if selected[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                        q.append([next_x, next_y])
                        count += 1
                        visited[next_x][next_y] = 1
                except AssertionError:
                    pass
        return count == 7

    def is_possible(som_count: int, total_count: int, x: int, y: int):
        if total_count == 7:
            prev_x, prev_y = prev_position(x, y)
            if som_count >= 4 and is_connected(prev_x, prev_y):
                global ret
                ret += 1
            return
        elif x == n:
            return

        next_x, next_y = get_next_position(x, y)

        selected[x][y] = 1
        if board[x][y] == 'S':
            is_possible(som_count + 1, total_count + 1, next_x, next_y)
        else:
            is_possible(som_count, total_count + 1, next_x, next_y)
        selected[x][y] = 0

        is_possible(som_count, total_count, next_x, next_y)

    global ret
    ret = 0
    is_possible(0, 0, 0, 0)
    print(ret)


solution()
