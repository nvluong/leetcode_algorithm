class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        s1 = ""
        s2 = ""
        while l <= r:
            if s[l] != s[r]:
                s1 = s[:l] + s[l+1:]
                s2 = s[:r] + s[r+1:]
                break

            l+=1
            r-=1
        if s1 == s1[::-1] or s2 == s2[::-1]:
            return True
        return False


sol = Solution()
s = "deeee"
print(sol.validPalindrome(s))