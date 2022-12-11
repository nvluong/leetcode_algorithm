class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]]+=1
        li = sorted(dict, reverse=True)
        if len(li) < 3:
            return max(li)
        return li[2]

sol = Solution()
nums = [2,2,3,1]
print(sol.thirdMax(nums))