class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        x = set()
        y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
        print(x)
        print(y)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in x or j in y:
                    matrix[i][j] = 0
        return matrix




sol = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(sol.setZeroes(matrix))