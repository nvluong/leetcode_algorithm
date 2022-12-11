class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        n = len(nums)
        r = n-1
        while l <= r:
            mid = int((l+r)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l

sol = Solution()
nums = [1,3,5,6,6]
target = 7
print(sol.searchInsert(nums, target))