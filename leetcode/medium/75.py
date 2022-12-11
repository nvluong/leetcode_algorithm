class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = len(nums)-1
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w +=1
                r+=1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b-=1
            elif nums[w] == 1:
                w+=1
        return nums


sol = Solution()
nums = [2,0,2,1,1,0]
print(sol.sortColors(nums))