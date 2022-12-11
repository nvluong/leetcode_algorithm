import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = 1
        r = int(math.sqrt(c))

        while l <= r:

            a = pow(l, 2) + pow(r, 2)

            if a == c:
                return True
            elif a > c:
                r -=1
            else:
                l +=1
        return False

sol = Solution()
c = 5
print(sol.judgeSquareSum(c))