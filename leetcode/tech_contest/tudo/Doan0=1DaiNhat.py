class Solution:
    def findMaxLength(self,nums):
        max_len = 0
        rsum = 0
        max_map = {}
        max_map[0] = -1
        for i in range(0, len(nums)):
            if nums[i] == 1:
                rsum += 1
            else:
                rsum -= 1

            if rsum in max_map:
                max_len = max(max_len, i - max_map.get(rsum))
            else:
                max_map[rsum] = i

        return max_len
sol = Solution()
# nums = [0,1,0,1,1,0,0,1,0,1]
nums = [0,0,0,0,1,1,1,1]
#[0101100101]
print(sol.findMaxLength(nums))
