class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else: dic[i] = 1
        for key, val in dic.items():
            if val == 1:
                return key
    def XoR_test(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            pass
sol = Solution()
nums = [1,2,1,2,1,4]
print(sol.singleNumber(nums))