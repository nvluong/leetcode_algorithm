
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1 = 0
        l2 = 0
        list_tmp = []
        len1 = len(list1)
        len2 = len(list2)

        while (l2 <= len2 - 1) and (l1 <= len1 - 1) :
            if list1[l1] == list2[l2]:
                print(list1[l1] , "= ", list2[l2])
                list_tmp.append(list1[l1])
                list_tmp.append(list2[l2])
                print(list_tmp)
                l1+=1
                l2+=1
            elif list1[l1] < list2[l2]:
                print(list1[l1], "< ", list2[l2])
                list_tmp.append(list1[l1])
                print(list_tmp)
                l1+=1
            else:
                print(list1[l1], "> ", list2[l2])
                list_tmp.append(list2[l2])
                print(list_tmp)
                l2+=1
        if l1 != len1:
            for i in range(l1, len1):
                list_tmp.append(list1[i])
        if l2 != len2:
            for i in range(l2, len2):
                list_tmp.append(list2[i])
        return list_tmp

sol = Solution()
list1 = [1,3,4,8,9]
list2 = [0,2,3,4,5,6,7]
print(sol.mergeTwoLists(list1, list2))
