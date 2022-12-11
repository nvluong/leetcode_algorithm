class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 1:
            return words
        i = 0
        while i < len(words)-1:
            # print(words)
            if sorted(words[i+1]) == sorted(words[i]):
                print(words)
                words.pop(i+1)
                # print("w ", words)
                i -= 1  # bởi vì sau khi pop đi thì sẽ giảm đi 1 đơn vị
            i += 1
        return words

sol = Solution()
words = ["abba","baba","bbaa","cd","cd"]
print(sol.removeAnagrams(words))