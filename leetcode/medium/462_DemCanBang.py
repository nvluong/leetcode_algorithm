class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        n = len(nums)
        dem1 = 0
        dem2 = 0
        if n%2 !=0:
            mid = nums[int(n/2)]
            print(mid)
            for i in nums:
                dem1+= abs(mid-i)
            return dem1
        else:
            mid = nums[int(n / 2)]
            mid1 = nums[int(n / 2)-1]
            for i in nums:
                dem1 += abs(mid - i)
                dem2 += abs((mid1-i))
            return min(dem1, dem2)
sol = Solution()
nums = [1,10,2,9]
print(sol.minMoves2(nums))