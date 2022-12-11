import math


class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        def check(mid):
            dem = 0
            print("mid", mid)
            for i in range(len(quantities)):
                b = quantities[i]
                if (b % mid) > 0:
                    dem += int(b/mid)+1
                else:
                    dem += int(b/mid)
            print("dem ", dem)
            if dem > n+1:
                return False
            else:
                return True
        l = 0
        r = max(quantities)
        while l < r - 1:
            print("l r", l, r)
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r


sol = Solution()
n = 7
quantities = [15, 10, 10]
print(sol.minimizedMaximum(n, quantities))
