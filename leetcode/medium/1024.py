class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        max1 = 0
        li = []

        a = 0
        b = 0

        clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        print(clips)
        if clips[0][1] >= time and clips[0][0] == 0:
            return 1
        if clips[0][0] != 0:
            return -1

        start = clips[0]
        start_tmp = clips[0]
        li.append(start)
        for i in range(len(clips)):
            if clips[i][0] == start[0]:
                continue
            else:
                start = clips[i]
                if clips[i][0] <= start_tmp[1]:
                    print(clips[i]," <= ",start_tmp)
                    b = clips[i]
                    if max1 < clips[i][1]:
                        max1 = clips[i][1]
                        a = clips[i]


                else:
                    print("a ", a)
                    print(clips[i], " > ", start_tmp)
                    b = clips[i]
                    print("li1", li)
                    if a!=0 and li[-1][1] < time:
                        start_tmp = a
                        print("st", start_tmp)

                        li.append(a)
                    else:
                        break
                    print("li12", li)


        # print(li)

        if b!=0 and b[0] <= li[-1][1] and b[1] > li[-1][1] and li[-1][1] < time:
            li.append(b)
        # print("li ", li)
        if li[-1][1] < time:
            return -1
        return li


sol = Solution()
# #
# clips = [[0,2],[4,7],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# time = 9
# clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
# clips = [[0,2],[8,10],[1,9],[1,5]]
# time = 10
# clips = [[0,2],[1,6],[3,10]]
# time = 10
# clips = [[0,2],[4,6]]
# time = 5

clips = [[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54],[50,55],[51,56],[52,57],[53,58],[54,59],[55,60],[56,61],[57,62],[58,63],[59,64]]

time = 50
print(sol.videoStitching(clips, time))
