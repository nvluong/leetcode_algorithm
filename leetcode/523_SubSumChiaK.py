class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict_tmp = {0:-1}
        s = 0
        for i, n in enumerate(nums):
            s += n
            a = s%k
            if a not in dict_tmp:
                dict_tmp[a] = i
            elif i - dict_tmp[a] > 1:
                return True
        return False



nums = [1, 2, 12]
k = 13
sol = Solution()
print(sol.checkSubarraySum(nums, k))
