class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = ''.join(ch for ch in s if ch.isalnum())
        str = str.lower()
        b = str[::-1]

        if b == str:
            return True
        else:
            return False

sol = Solution()
s = "A man, a plan, a canal: Panama +"
print(sol.isPalindrome(s))
