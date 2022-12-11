class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        list_pref = []
        list_post = []
        s = 1
        s1 = 1

        for i in range(n):
            if nums[i] == 0:
                s = 1
                list_pref.append(0)
                continue
            s *= nums[i]
            list_pref.append(s)
        # print(list_pref)

        for i in reversed(range(n)):
            if nums[i] == 0:
                s1 = 1
                list_post.append(0)
                continue
            s1 *= nums[i]
            list_post.append(s1)
        # print(list_post)
        max1 = max(list_pref)
        max2 = max(list_post)
        return max(max1, max2)



sol = Solution()

nums = [2,3,0,-2,4,10,-2,-2,4,5]
print(sol.maxProduct(nums))