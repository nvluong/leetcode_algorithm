class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        print(potions)
        li = []
        for i in range(len(spells)):
            l = 0
            r = len(potions)-1
            a = float(float(success)/spells[i])
            print("suc ", success, "spell ", spells[i])
            print("a ", a)
            flag = 0
            b = 0
            while l <= r:
                print("l ", l,  "r ", r)
                mid = int((l+r)/2)
                print("mid l", mid)
                if potions[mid] > a :
                    print("a ", a)
                    print(potions[mid], " > ", a)

                    r = mid - 1
                elif potions[mid] == a:

                    print(potions[mid], a)
                    print("len ", len(potions))
                    print("mid1 ", mid)
                    print("S ", len(potions) - mid - 1)

                    print("li ", li)
                    flag = 1
                    r = mid - 1
                    b = mid
                    # break
                else:
                    print(potions[mid], " < ", a)
                    l = mid+1


            if flag == 0:
                print("flag ", flag)
                print("len ", len(potions))
                print("l1 ", l)
                li.append(len(potions) - l)
                print("li ", li)
            else:
                li.append(len(potions) - b)
            print("-------------------------------------------")
        return li




sol = Solution()
spells = [40,11,24,28,40,22,26,38,28,10,31,16,10,37,13,21,9,22,21,18,34,2,40,40,6,16,9,14,14,15,37,15,32,4,27,20,24,12,26,39,32,39,20,19,22,33,2,22,9,18,12,5]
potions = [31,40,29,19,27,16,25,8,33,25,36,21,7,27,40,24,18,26,32,25,22,21,38,22,37,34,15,36,21,22,37,14,31,20,36,27,28,32,21,26,33,37,27,39,19,36,20,23,25,39,40]

success = 600

# spells = [5,1,3]
# potions = [1,2,3,4,5]
# success = 7
print(sol.successfulPairs(spells, potions, success))
