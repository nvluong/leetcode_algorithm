class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        li = s.split()
        return " ".join(li[:k])

sol = Solution()
s = "Hello how are you Contestant"
k = 4
print(sol.truncateSentence(s, k))
