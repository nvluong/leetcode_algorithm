class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = nums[:]
        a.sort()
        for j in range(len(nums)):
            dem = 0
            for i in range(len(nums)):
                if a[i] == nums[(i+j)%len(nums)]:
                    dem+=1
            if dem == len(nums):
                return True
        return False
sol = Solution()
nums = [1,2,3]
print(sol.check(nums))