class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        prev = nums[1]-nums[0]
        if prev != 0:
            dem = 2
        else:
            dem = 1
        for i in range(2,len(nums)):
            diff =  nums[i]- nums[i-1]
            if (diff > 0 and prev <= 0) or ( diff < 0 and prev >= 0):
                dem+=1
                prev = diff
        return dem

sol = Solution()
nums = [0,0]
print(sol.wiggleMaxLength(nums))
