class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i, n in enumerate(nums):
            dict[i] = n
        print(dict)
sol = Solution()
nums = [0,0,0,0,1,1,1,1,0,1,0,0,1,1]
print(sol.findMaxLength(nums))
