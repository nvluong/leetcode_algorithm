class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dem = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                print(nums)
                print(nums[i-1], nums[i])
                lech = nums[i-1]-nums[i]+1
                print("lech ", lech)
                dem+=lech
                nums[i] = nums[i-1]+1
        print(nums)
        return dem

sol = Solution()
nums = [3,2,1,2,1,7,2]
print(sol.minIncrementForUnique(nums))