class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = nums[::-1]
        for i in range(1,len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
        # print(nums)
            if b[i-1] != 0:
                b[i] *= b[i-1]
        print(b)
        print(nums)
        print(nums+b)







sol = Solution()

nums = [-2,2,0,3,-2,-6,-2]
print(sol.maxProduct(nums))