class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        l = 0
        r = len(colors)-1
        s = 0
        for i in range(len(colors)):
            if colors[l] != colors[i]:
                s = max(s, i-l)
            if colors[r] != colors[i]:
                s = max(s, r-i)
        return s

sol = Solution()
colors = [4,4,4,11,4,4,11,4,4,4,4,4]
print(sol.maxDistance(colors))