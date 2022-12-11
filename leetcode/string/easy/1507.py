class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        dict_tmp = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                    "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

        date = date.split()
        date_1 = date[0][:-2]
        if len(date_1) == 1:
            date_1 = "0"+str(date_1)
        date_2 = dict_tmp[date[1]]
        date_3 = date[2]
        return date_3+"-"+date_2+"-"+date_1


sol = Solution()
date = "26th May 1960"
print(sol.reformatDate(date))