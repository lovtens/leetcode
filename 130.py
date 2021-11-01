# https://leetcode.com/problems/surrounded-regions/
# dfs
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i: int, j: int, visit):
            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                return False

            visit[i][j] = True

            # left
            if j > 0 and not visit[i][j - 1] and board[i][j - 1] == 'O':
                left = dfs(i, j - 1, visit)
                if not left:
                    return False
            # right
            if j < len(board[0]) - 1 and not visit[i][j + 1] and board[i][j + 1] == 'O':
                right = dfs(i, j + 1, visit)
                if not right:
                    return False
            # up
            if i > 0 and not visit[i - 1][j] and board[i - 1][j] == 'O':
                up = dfs(i - 1, j, visit)
                if not up:
                    return False
            # down
            if i < len(board) - 1 and not visit[i + 1][j] and board[i + 1][j] == 'O':
                down = dfs(i + 1, j, visit)
                if not down:
                    return False

            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    visit = []
                    for _ in range(len(board)):
                        visit.append([False] * len(board[0]))

                    if dfs(i, j, visit):
                        for x in range(len(visit)):
                            for y in range(len(visit[0])):
                                if visit[x][y]:
                                    board[x][y] = 'X'
