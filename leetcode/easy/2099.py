class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        a = [(j,i) for i, j in enumerate(nums)]
        print(a)
        a.sort(key= lambda x:x, reverse=True)
        print(a)
        a = a[:k]
        print(a)
        a.sort(key=lambda x:x[1])
        print(a)
        li = []
        for i in a:
            li.append(i[0])
        return li

sol = Solution()
nums = [2,1,3,3]
k = 2
print(sol.maxSubsequence(nums, k))
