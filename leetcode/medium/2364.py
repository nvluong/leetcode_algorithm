class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        li = []
        for i, n in enumerate(nums):
            li.append(i)
        print(li)
        dic = {}
        for i in range(len(li)):
            dic[li[i]] = nums[i]
        print(dic)

sol = Solution()
nums = [4,1,3,3]
print(sol.countBadPairs(nums))