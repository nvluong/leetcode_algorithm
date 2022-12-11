class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1 = nums[0]
        max2 = nums[1]-nums[0]
        for i in range(len(nums)):
            min1 = min(min1, nums[i])
            print("min ", min1)
            max2 = max(max2,nums[i] - min1)
            print("max ", max2)

        if max2 <= 0:
            return -1
        else:
            return max2
sol = Solution()
nums = [9,4,3,2]
print(sol.maximumDifference(nums))