class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums) - 1
        if len(nums) == 1:
            return 0
        if len(nums) > 1:
            if nums[r] > nums[r - 1]:
                return r
            if nums[0] > nums[1]:
                return 0
        l = 1
        r = len(nums) - 2
        while l <= r:

            if nums[l + 1] < nums[l] and nums[l - 1] < nums[l]:
                return l
            if nums[r + 1] < nums[r] and nums[r - 1] < nums[r]:
                return r
            l += 1
            r -= 1
sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))