class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        li = [[i,j] for i, j in zip(difficulty, profit)]
        li.sort(key= lambda x:x[0])

        print(li)
        j = 0
        max_tmp = 0
        s = 0
        for i in sorted(worker):
            while j < len(li):
                if i >= li[j][0]:
                    max_tmp = max(max_tmp, li[j][1])
                    j+=1
                else:
                    break
            s+=max_tmp
        return s


sol = Solution()
difficulty = [68,35,52,47,86]
# difficulty = [68,35,81,47,86]

profit =     [67,17,1,81,3]
# profit =     [67,17,100,81,3]
worker = [92,10,85,84,82]
print(sol.maxProfitAssignment(difficulty, profit, worker))