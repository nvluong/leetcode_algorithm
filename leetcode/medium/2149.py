class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li = []
        li2 = []
        for i in range(len(nums)):
            if nums[i] < 0:
                li.append(nums[i])
            else:
                li2.append(nums[i])
        li_tmp = []
        for i in range(len(li)):
            li_tmp.append(li2[i])
            li_tmp.append(li[i])
        return li_tmp

sol = Solution()
nums = [3,1,-2,-5,2,-4]
print(sol.rearrangeArray(nums))