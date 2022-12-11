import math


class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = math.pow(10,9)+7
        n = len(nums)
        list_congdon = [0]*n
        print(list_congdon)
        for i in requests:
            list_congdon[i[0]] += 1
            if i[1] + 1 < n:
                list_congdon[i[1]+1] -= 1
        print(list_congdon)
        list_tmp = []
        s = 0
        for i in range(len(list_congdon)):
            s+=list_congdon[i]
            list_tmp.append(s)
        print(list_tmp)
        list_tmp.sort()
        print("listtmp ", list_tmp)
        nums.sort()
        print("nums ", nums)
        s = 0
        for i in range(len(nums)):
            s+= nums[i]*list_tmp[i]
        return int(s % MOD)
nums =[1,8,5,5,2]

requests = [[4,4],[3,4],[4,4],[2,4],[0,0]]

sol = Solution()
print(sol.maxSumRangeQuery(nums, requests))