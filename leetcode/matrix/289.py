class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        matrix_tmp = [[0 for _ in range(m)] for _ in range(n)]
        matrix = [[0 for _ in range(m+2)] for _ in range(n+2)]

        # print(matrix)
        # print(matrix_tmp)
        for i in range(1,n+1):
            for j in range(1,m+1):
                matrix[i][j] = board[i-1][j-1]
        # print(matrix)

        for i in range(1, n+1):
            for j in range(1, m+1):
                s = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + \
                    matrix[i][j - 1] + matrix[i][j + 1] + \
                    matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]

                if matrix[i][j] == 0 and s == 3:
                    matrix_tmp[i - 1][j - 1] = 1
                if matrix[i][j] == 1:
                    if s < 2:
                        matrix_tmp[i - 1][j - 1] = 0
                    if s == 2 or s == 3:
                        matrix_tmp[i - 1][j - 1] = 1
                    if s > 3:
                        matrix_tmp[i - 1][j - 1] = 0
        for i in range(n):
            for j in range(m):
                board[i][j] = matrix_tmp[i][j]
        return board


sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(sol.gameOfLife(board))
