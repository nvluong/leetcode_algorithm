class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}

        for i, n in enumerate(nums):
            if n not in dict:
                dict[n] = i
            else:
                return n

nums = [1,2,3,2,4]
sol = Solution()
print(sol.findDuplicate(nums))
