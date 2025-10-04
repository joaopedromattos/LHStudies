

class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        def isOverlap(last_s, last_e, cur_s, cur_e):
            return cur_s < last_e

        remove = 0
        intervals.sort(key=lambda x: x[1])
        print("After first sort", intervals)
        # intervals.sort(key=lambda x: x[1])
        # print("After second sort", intervals)

        s, e = [intervals[0][0]], [intervals[0][1]]

        for cur_s, cur_e in intervals[1:]:
            if isOverlap(s[-1], e[-1], cur_s, cur_e):
                remove += 1
            else:
                s.append(cur_s)
                e.append(cur_e)


        return remove

        