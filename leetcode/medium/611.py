class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = nums[:]
        b.sort()
        print(b)
        l = 0
        r = len(b)-1
        dem = 0
        while l <= r:
            if b[l] + b[r] > b[r-1] and b[l] + b[r-1] > b[l] and b[r] + b[r-1] > b[l]:
                dem+=1
                r-=1
            else:
                l+=1
        return dem



sol = Solution()
nums = [4,2,3,4]
print(sol.triangleNumber(nums))