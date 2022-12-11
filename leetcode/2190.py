import collections


class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        count = {}
        ans = 0
        val = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i+1] not in count:
                    count[nums[i + 1]] = 1
                else:
                    count[nums[i+1]] +=1
                if count[nums[i + 1]] > val:

                    val = count[nums[i + 1]]
                    ans = nums[i + 1]
        print(count)
        return ans

sol = Solution()
nums = [1,1,1,2,1,100,200,12,1,100,100, 2]
key = 1
print(sol.mostFrequent(nums, key))