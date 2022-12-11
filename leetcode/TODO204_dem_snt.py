import math
class Solution(object):
    def snt(self, a):
        if a < 2: return 0
        else:
            m = int(math.sqrt(a))
            for i in range(2, m+1):
                if a % i == 0: return 0
            else: return 1
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(n):

            if self.snt(i):
                print(i)
                count+=1
        return count

sol = Solution()
n = 10
print(sol.countPrimes(n))