class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        n = len(nums)
        if n == 0:
            return 0
        dem = 0
        max = 0
        for i in range(n-1):
            if nums[i] == nums[i+1] - 1:
                print("dem1 ", dem)
                print("num ", nums[i], "num ", nums[i+1])
                dem+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                dem = 0
            if max <= dem:
                max = dem
        return max+1



sol = Solution()
nums = [1,2,0,1]
print(sol.longestConsecutive(nums))

