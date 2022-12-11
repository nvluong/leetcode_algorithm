class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max1 = sum(accounts[0])
        for i in accounts:
            max1 = max(max1,sum(i))
        return max1