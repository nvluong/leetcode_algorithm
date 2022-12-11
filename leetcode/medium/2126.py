class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        li = []
        li1 = []
        li2 = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                li.append(nums[i])
            elif nums[i] == pivot:
                li1.append(nums[i])
            else:
                li2.append(nums[i])
        return li+li1+li2

sol = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
print(sol.pivotArray(nums, pivot))