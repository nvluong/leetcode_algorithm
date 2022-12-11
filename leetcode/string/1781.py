class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        tong = 0
        for i in range(len(s)):
            dict = {}
            for j in range(i, len(s)):
                # print("s ", s[j])
                print("s ", s[:j])

                dict.setdefault(s[j], 0)
                dict[s[j]] += 1
                print(dict)
                tong += max(dict.values()) - min(dict.values())

                print("tong", tong)
        # print("----------")

        return tong


sol = Solution()
s = "aabcbaa"
# s = "bcbaa"
print(sol.beautySum(s))
