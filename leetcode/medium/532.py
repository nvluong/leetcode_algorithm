import collections
import math


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dict_1 = {}
        dem = 0
        for i, n in enumerate(nums):
            if n not in dict_1:
                dict_1[n] = 1
            else:
                dict_1[n]+=1
        print(dict_1)
        if k == 0:
            for key, v in dict_1.items():
                if v > 1:
                    dem+=1
        else:
            for key, v in dict_1.items():
                print(key+k, dict_1)
                if key+k in dict_1:
                    dem+=1

        return dem


sol = Solution()
nums = [3,1,4,1,5]
k = 2
print(sol.findPairs(nums, k))
