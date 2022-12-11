class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """

        def count_time(a):
            dem = 0
            b = 0
            start_time = a[0]
            for i in range(len(a)):
                gio_now = int(a[i][:2])
                phut_now = int(a[i][3:])

                gio_start = int(start_time[:2])
                phut_start = int(start_time[3:])

                if gio_now == gio_start:
                    b = b + phut_now - phut_start
                else:
                    b = b + 60 * (gio_now - gio_start) - phut_start + phut_now
                dem += 1
                if dem == 3 and b <= 60:
                    return 1
                if b > 60:
                    b = 0
                    dem = 0
                start_time = a[i]

        li_tmp = []
        dict = {}
        for i , n in enumerate(keyName):
            if n not in dict:
                dict[n] = [keyTime[i]]
            else:
                dict[n].append(keyTime[i])

        for k, v in dict.items():
            print("v", v)
            if count_time(v) == 1:
                li_tmp.append(k)
        return li_tmp









sol = Solution()
keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]


keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
print(sol.alertNames(keyName, keyTime))