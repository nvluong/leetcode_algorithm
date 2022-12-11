class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = 1
        l = 0
        while l < len(nums)-1:
            if nums[l] != nums[l+1]:
                nums[r] = nums[l+1]
                r+=1
            l+=1
        return nums

    def cach2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = 1
        l = 0
        tmp = nums[0]
        while l < len(nums) - 1:
            if tmp != nums[l+1]:
                tmp = nums[l+1]
                nums[r] = tmp
                r+=1
            l+=1
        return nums



sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]

# nums = [1,1,2]
print(sol.cach2(nums))