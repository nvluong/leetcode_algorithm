class Solution(object):



    # dict_tmp = {}
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        import string

        alpha = string.ascii_lowercase
        dict_tmp = {' ':' '}
        i = 0
        for k in key:

            if k not in dict_tmp:
                dict_tmp[k] = alpha[i]
                i += 1


        res = ""
        for m in message:
            res += dict_tmp[m]
        return res


sol = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(sol.decodeMessage(key, message))
