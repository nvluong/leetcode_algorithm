class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        end = len(arr)
        temp = arr[end - 1]
        print("Tem p ", temp)
        arr[end - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > temp:
                print("a i ", arr[i],  "temp ", temp)
                arr[i], temp = temp, arr[i]
                print(arr)
            else:
                print("a i ", arr[i],  "temp ", temp)
                arr[i] = temp
                print(arr)
        return arr

sol = Solution()
arr = [17,18,5,4,6,1]
print(sol.replaceElements(arr))
