class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        nums = nums[::-1]
        print(nums)
        return nums[k-1]


sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(sol.findKthLargest(nums,k))