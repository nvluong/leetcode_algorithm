class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = {}
        for word in words:
            sk = "".join(sorted(word))
            print("sk ", sk)
            if sk in d:
                d[sk].append(word)
            else:
                d[sk] = [word]
        print(d)
        return d.values()



sol = Solution()
words = ["abba","baba","bbaa","cd","cd"]
print(sol.removeAnagrams(words))