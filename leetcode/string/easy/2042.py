class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = list()
        words = s.split(" ")
        for word in words:
            if word.isdigit():
                print(word)
                lst.append(int(word))
        for i in range(0, len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                return False
        return True



sol = Solution()
s = "1 3 6 12"
print(sol.areNumbersAscending(s))
