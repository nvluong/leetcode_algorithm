class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        b = [-1]*len(arr)
        for i in range(len(arr)):
            b[i] = arr[i]
        b.sort()
        dict = {}
        dem = 1
        for i, n in enumerate(b):
            if n not in dict:
                dict[n] = dem
                dem+=1
        # print(dict)
        list_tmp = []
        for i in arr:
            list_tmp.append(dict[i])
        return list_tmp



sol = Solution()
arr = [37, 12,12, 28, 9, 100, 56, 80, 5, 12]
#     [5,9,12,12,28,37,56,80,100]
print(sol.arrayRankTransform(arr))