import collections


class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = collections.Counter(nums)
        print(a)
        for i in a.values():
            print(i)
            if i % 2 != 0:
                return False
        return True

sol = Solution()
nums = [3,2,3,2,2,2]
print(sol.divideArray(nums))