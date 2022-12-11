class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            print(prefix)
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            print("postfix ", postfix)
            res[i] *= postfix
            postfix *= nums[i]
            print("res ", res)
        return res




sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))