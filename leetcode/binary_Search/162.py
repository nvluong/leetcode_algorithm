class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 1, len(nums) - 2
        while l <= r:
            m = l + (r - l) // 2
            print("m = ", m)
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                print(nums[m] , ">", nums[m-1], "and ", nums[m], " > ", nums[m+1])
                return m

            if nums[m + 1] > nums[m]:
                l = m + 1
            elif nums[m - 1] > nums[m]:
                r = m - 1
sol = Solution()
nums = [1,2,3,1]
print(sol.findPeakElement(nums))