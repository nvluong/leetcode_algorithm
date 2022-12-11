class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == k:
            return nums
        else:
            b = k % n
            a = nums[n-b:n]
            print("a ", a)
            b1 = nums[:n-b]
            print("b1 ", b1)
            for i in reversed(range(len(b1))):
                print("hihi",b1[i])
                nums[i+b] = b1[i]
            for i in range(len(a)):
                nums[i] = a[i]
        return nums


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
print(sol.rotate(nums, k))
