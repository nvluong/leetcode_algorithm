class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:  # List only has 1 element
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        if nums[0] > nums[1]:
            return 0

        left = 1
        right = len(nums) - 2
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid - 1] < nums[mid]) and (nums[mid + 1] < nums[mid]):
                return mid
            elif (nums[mid - 1] > nums[mid]) and (nums[mid + 1] < nums[mid]):

                right = mid - 1
            else:
                left = mid + 1
sol = Solution()
nums = [0,10,5,2]
print(sol.findPeakElement(nums))