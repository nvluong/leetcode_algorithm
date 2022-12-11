class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        myset = set(wordDict)

        def rec(sub):
            size = len(sub)
            if size == 0:
                return True
            for i in range(1, size + 1):
                if sub[0:i] in myset:
                    if rec(sub[i:]):
                        return True
            return False

        return rec(s)

sol = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(sol.wordBreak(s, wordDict))