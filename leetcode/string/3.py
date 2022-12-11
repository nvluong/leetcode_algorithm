class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_tmp = {}
        dem = 0
        max1 = 0
        i = 0
        while i <= len(s) - 1:
            if s[i] not in dict_tmp:
                dict_tmp[s[i]] = i
                dem += 1
                i += 1
            else:
                dem = 0
                i = dict_tmp[s[i]] + 1
                print(s[i])
                dict_tmp.clear()
            max1 = max(max1, dem)

        return max1


sol = Solution()
# s = "dvadf"
s = "bbbb"
print(sol.lengthOfLongestSubstring(s))