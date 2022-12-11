class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # dict_i = {}
        # dict_j = {}
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 1:
        #             if i not in dict_i:
        #                 dict_i[i] = 1
        #             else:
        #                 dict_i[i] +=1
        #             if j not in dict_j:
        #                 dict_j[j] = 1
        #             else:
        #                 dict_j[j] +=1
        # print(dict_i, dict_j)
        # retVal = 0
        # for r in range(len(mat)):
        #     for c in range(len(mat[r])):
        #         if mat[r][c] == 1 and dict_j[c] == 1 and dict_i[r] == 1:
        #             retVal += 1
        #
        # return retVal

        rows = [sum(row) for row in mat]
        print(rows)
        cols = [sum(col) for col in zip(*mat)]
        print(cols)
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res


sol = Solution()
mat = [[1,0,0],[0,0,1],[1,0,0]]
print(sol.numSpecial(mat))