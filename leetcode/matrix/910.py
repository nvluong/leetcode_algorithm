class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        min1 = nums[n-1] - nums[0]
        for i in range(n-1):
            j = i+1
            print("nums[0]+k ", nums[0]+k, "nums[j] - k", nums[j] - k)
            low = min(nums[0] + k, nums[j] - k)
            print("low ", low)
            print("nums[n-1] - k ", nums[n-1] - k, "nums[i] + k", nums[i] + k)
            high = max(nums[n-1] - k, nums[i] + k)
            print("high ", high)

            min1 = min(min1, high - low)
            print("min", min1)
        return min1




sol = Solution()
nums = [1,3,6]
k = 3

print(sol.smallestRangeII(nums, k))