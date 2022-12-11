import collections


class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        frequency = collections.Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))


sol = Solution()
nums = [-1,1,-6,4,5,-6,1,4,1]
print(sol.frequencySort(nums))
#[5, -1, 4, 4, -6, -6, 1, 1, 1]