class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_tmp = {}
        for i, n in enumerate(numbers):
            a = target-n
            if a in dict_tmp:
                return dict_tmp[a]+1, i+1
            dict_tmp[n] = i
sol = Solution()
numbers = [-1,0]
target = -1

print(sol.twoSum(numbers, target))