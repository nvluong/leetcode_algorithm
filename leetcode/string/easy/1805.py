class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = word + "l"
        s = ""
        dem = set()
        for i in range(len(word)):
            if word[i].isdigit():
                s+=word[i]
            else:
                if s.isdigit():
                    a = int(s)
                    # print("a", a)
                    dem.add(a)
                s =""
        return len(dem)


sol = Solution()
word = "a123bc34d8ef34"
print(sol.numDifferentIntegers(word))
