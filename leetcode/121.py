class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_tmp = 0
        min_tmp = prices[0]
        for i in prices:
            min_tmp = min(min_tmp, i)
            s = i - min_tmp
            max_tmp = max(max_tmp, s)
        return max_tmp
sol = Solution()
prices = [7,1,5,3,6,4]
# prices = [7,1,2,3,6,4]
print(sol.maxProfit(prices))