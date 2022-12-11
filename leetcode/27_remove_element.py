class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # list_temp = []
        # for i in nums:
        #     if i != val:
        #         list_temp.append(i)
        # print(list_temp)
        # return len(list_temp)

        l = 0
        r = 0
        while l < len(nums):
            if nums[l] == val:
                r = l
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        return nums



sol = Solution()
nums = [3,2,2,3]
val = 3

print(sol.removeElement(nums, val))
