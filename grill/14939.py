import sys
import math

min_toggle = math.inf
backtrack_count = 0


def solution():
    n = 10
    board = []
    for _ in range(n):
        board.append(list(map(lambda x: int(x == 'O'), list(sys.stdin.readline()))))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def toggle(tmp_board, x, y):
        tmp_board[x][y] = int(not tmp_board[x][y])
        for i in range(4):
            try:
                xx = x + dx[i]
                yy = y + dy[i]
                assert 0 <= xx < n and 0 <= yy < n
                tmp_board[xx][yy] = int(not tmp_board[xx][yy])
            except AssertionError:
                pass

    pushed = ((1 << n) - 1)

    subset = pushed
    while True:
        tmp_board = []
        for i in range(n):
            tmp_board.append(board[i][:])
        toggle_count = 0
        for i in range(n):
            if subset & (1 << i):
                toggle_count += 1
                # pushed
                x = i // n
                y = i % n
                toggle(tmp_board, x, y)

        for i in range(n, n ** 2):
            x = i // n
            y = i % n
            if tmp_board[x - 1][y]:
                toggle_count += 1
                toggle(tmp_board, x, y)

        if sum(tmp_board[-1]) == 0:
            global min_toggle
            min_toggle = min(min_toggle, toggle_count)

        if not subset:
            break
        subset = ((subset - 1) & pushed)

    if min_toggle == math.inf:
        print(-1)
    else:
        print(min_toggle)


solution()
