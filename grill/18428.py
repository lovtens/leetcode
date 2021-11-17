import sys


def solution():
    n = int(sys.stdin.readline().strip())
    board = []
    for _ in range(n):
        board.append(sys.stdin.readline().strip().split())

    students = [] # pair
    teachers = [] # pair
    xs = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                teachers.append((i,j))
            elif board[i][j] == 'S':
                students.append((i,j))
            else:
                xs.append((i,j))

    def check_board():
        for t_x, t_y in teachers:
            # right
            i = t_x
            j = t_y
            while j < n:
                if board[i][j] == 'O':
                    break
                if board[i][j] == 'S':
                    return False
                j += 1
            # left
            i = t_x
            j = t_y
            while j >= 0:
                if board[i][j] == 'O':
                    break
                if board[i][j] == 'S':
                    return False
                j -= 1
            # up
            i = t_x
            j = t_y
            while i >= 0:
                if board[i][j] == 'O':
                    break
                if board[i][j] == 'S':
                    return False
                i -= 1
            # down
            i = t_x
            j = t_y
            while i < n:
                if board[i][j] == 'O':
                    break
                if board[i][j] == 'S':
                    return False
                i += 1
        return True

    def is_possible(x_idx: int, obj_left: int):
        if obj_left == 0:
            return check_board()
        if x_idx == len(xs):
            return check_board()
        x, y = xs[x_idx]
        board[x][y] = 'O'
        if is_possible(x_idx+1, obj_left - 1):
            return True
        board[x][y] = 'X'
        if is_possible(x_idx+1, obj_left):
            return True

        return False

    if is_possible(0, 3):
        print("YES")
    else:
        print("NO")

solution()


# 4
# S S S X
# X X X X
# X X X X
# X X X X

# 4
# X S X T
# X X S X
# X X X X
# T T T X

# 5
# X X S X X
# X X X X X
# S X T X S
# X X X X X
# X X S X X


# 5
# X T X T X
# T X S X T
# X S S S X
# T X S X X
# X T X X X

# 5
# X S S S X
# T X X S X
# X T X S X
# X X T X S
# X X X T X


