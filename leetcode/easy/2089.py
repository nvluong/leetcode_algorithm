class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()

        list_tmp = []
        for i, n in enumerate( nums):
            if n == target:
                list_tmp.append(i)
        return list_tmp
sol = Solution()
nums = [100,1,100]
target = 100
print(sol.targetIndices(nums, target))
