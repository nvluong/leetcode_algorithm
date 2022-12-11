class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix[0])-1
        print(l, r)
        while l <= r:
            top, bottom = l, r
            for i in range(r - l):
                print("i ", i)
                temp = matrix[top][r-i]
                matrix[top][r-i] = matrix[bottom - i][r]
                matrix[bottom - i][r] = matrix[bottom][l+i]
                matrix[bottom][l + i] = matrix[top+i][l]
                matrix[top + i][l] = temp
            l+=1
            r-=1
        return matrix



sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.rotate(matrix))