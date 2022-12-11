class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        print("total ", total_sum)
        leftsum = 0
        for i, num in enumerate(nums):
            total_sum -= num
            print("total", total_sum)
            print("leftsum", leftsum)

            if leftsum == total_sum:
                return i
            leftsum += num
        return -1

sol = Solution()
nums = [1,7,3,6,5,6]
print(sol.pivotIndex(nums))