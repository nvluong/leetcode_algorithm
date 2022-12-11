class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        li = []
        for i in range(len(arr)):
            li.append((bin(arr[i]).count("1"), arr[i]))
        print(li)
        li.sort()

        for i in range(len(li)):
            arr[i] = li[i][1]
        return arr

sol = Solution()
arr = [1024,512,256,128,64,32,16,8,5,4,3,2,1]
print(sol.sortByBits(arr))