class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        lits = []
        max_val = max(candies)
        for i in candies:
            if i + extraCandies >= max_val:
                lits.append(True)
            else:
                lits.append(False)
        return lits

sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies,extraCandies))