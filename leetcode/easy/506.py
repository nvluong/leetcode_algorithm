class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        a = score[:]
        a.sort()
        a = a[::-1]

        dict = {}
        for i, n in enumerate(a):
            if n not in dict:
                dict[n] = i+1

        for k, v in dict.items():
            if  v == 1:
                dict[k] = "Gold Medal"
            elif v == 2:
                dict[k] = "Silver Medal"
            elif v == 3:
                dict[k] = "Bronze Medal"
            else:
                dict[k] = str(v)

        li = []
        for i in range(len(score)):
            li.append(dict[score[i]])
        return li



sol = Solution()
score = [10,3,8,9,4]
print(sol.findRelativeRanks(score))