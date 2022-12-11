class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        li_str = s.split()
        print(li_str)
        li_str = sorted(li_str, key= lambda x:x[-1])
        print(li_str)
        a = " ".join([w[:-1] for w in li_str])
        return a


sol = Solution()
s = "is2 sentence4 This1 a3"
print(sol.sortSentence(s))