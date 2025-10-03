class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if intervals == []:
            return [newInterval]

        def isOverLap(last_s, last_e, cur_s, cur_e):
            print(last_s, last_e, cur_s, cur_e)
            overlap = False
            if cur_s <= last_s and cur_e >= last_e:
                last_s = cur_s
                overlap = True

            if cur_s <= last_e and cur_e > last_e:
                last_e = cur_e
                overlap = True

            if cur_e <= last_e:
                last_e = last_e
                overlap = True
            print("Before return", overlap, last_s, last_e)
            return overlap, last_s, last_e

        # for i in range(len(intervals)):
        #     _, intervals[i][0], intervals[i][1] = isOverLap(intervals[i][0], intervals[i][1], newInterval[0], newInterval[1])

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        print("Intervals", intervals)
        s, e = [intervals[0][0]], [intervals[0][1]]
        for i in range(1, len(intervals)):
            overlap, new_s, new_e = isOverLap(s[-1], e[-1], intervals[i][0], intervals[i][1])

            if overlap:
                s[-1] = new_s
                e[-1] = new_e
            else:
                s.append(intervals[i][0])
                e.append(intervals[i][1])

        return list(zip(s, e))


        
        