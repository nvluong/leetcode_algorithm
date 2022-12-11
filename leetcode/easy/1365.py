class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b = nums[:]
        b.sort()
        # print(b)
        dict = {}
        for i, n in enumerate(b):
            dict[i] = n
        print(dict)
        li = []
        val_list = list(dict.values())
        for i in nums:
            li.append(val_list.index(i))
        return li





sol = Solution()
nums = [8,1,2,2,3]
print(sol.smallerNumbersThanCurrent(nums))