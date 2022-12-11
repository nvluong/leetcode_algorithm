
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = []
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            prefix_sum.append(s)
        print(prefix_sum)
        total_sum = prefix_sum[len(nums) - 1]
        for i in range(len(nums)):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = total_sum - prefix_sum[i]
            if left_sum == right_sum:
                return i
        return -1

sol = Solution()
nums =  [1,7,3,6,5,6]
print(sol.pivotIndex(nums))