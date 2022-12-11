class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            s = nums[left] + nums[right]
            if s == target:
                return left, right
            elif s > target:
                right -= 1
            else:
                left += 1

    def twoSum2(self, nums, target):
        dic = dict()
        for i, s in enumerate(nums):
            a = target - s
            print(a, s,  dic)
            if a in dic:
                print(a,s, dic)
                return dic[a], i
            dic[s] = i

    def duyet_trau(self, nums, target):
        pass
sol = Solution()
nums = [2,4,3]
target = 6
print(sol.twoSum2(nums, target))