class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dem_duong = 0
        dem_am = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0:
                dem_am+=1
            if nums[i] > 0:
                dem_duong+=1
        if n == 3:
            return nums[0]*nums[1]*nums[2]
        else:
            if dem_duong == 1 and dem_am > 1:
                return nums[0]*nums[1]*nums[n-1]
            else:
                a = nums[n-1]*nums[n-2]*nums[n-3]
                b = nums[0]*nums[1]*nums[n-1]
                return max(a,b)





sol = Solution()
nums = [-100,-2,-3,1]
# nums = [1,2,3,4]
print(sol.maximumProduct(nums))
