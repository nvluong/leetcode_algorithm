class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_tmp = 0
        min_tmp = prices[0]
        s = 0
        for i in prices:
            min_tmp = min(min_tmp, i)
            s += i - min_tmp
            print("i1 ", i, " - min ", min_tmp)
            print("s1 ", s)
            if max_tmp <= s:
                print("s ", s)
                max_tmp = s
                min_tmp = i
                print("min ", i)
        return max_tmp
sol = Solution()
prices = [7,1,2,6,4]
# prices = [7,1,2,3,6,4]
print(sol.maxProfit(prices))