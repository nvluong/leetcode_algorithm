class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
        for i in range(n):
            for j in range(int(n/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]

                matrix[i][n-j-1] = temp
        for j in range(n):
            for i in range(int(n/2)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][j]
                matrix[n-1-i][j] = temp

        return matrix


sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.rotate(matrix))