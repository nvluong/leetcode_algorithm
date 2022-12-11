class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        list_tmp = []
        for i in bank:
            dem = 0
            for j in i:
                if j == "1":
                    dem+=1
            if dem != 0:
                list_tmp.append(dem)
        a = 0
        for i in range(len(list_tmp)-1):
            a+=list_tmp[i] * list_tmp[i+1]
        return a


sol = Solution()
bank = ["011001","000000","010100","001000"]
print(sol.numberOfBeams(bank))