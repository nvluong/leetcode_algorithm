class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        n = len(nums)
        r = n-1
        while l <= r:
            if nums[l] == target and nums[r] == target:
                return [l, r]
            if nums[l] < target:
                l+=1
            if nums[r] > target:
                r-=1
        return [-1,-1]

sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(sol.searchRange(nums, target))
