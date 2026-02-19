'''
Principle: Adjacent sorted intervals overlapping can be merged. If no additional interval can be merged, we are done.


'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        def overlap(interval1, interval2):
            case1 = interval1[0] <= interval2[0] <= interval1[1]
            case2 = interval1[0] <= interval2[1] <= interval1[1]
            case3 = interval2[0] <= interval1[0] and interval1[1] <= interval2[1]

            return case1 or case2 or case3

        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        

        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        final_ans = [intervals[0]]


        for cur_interval in intervals[1:]:
            if overlap(final_ans[-1], cur_interval):
                final_ans[-1] = merge(final_ans[-1], cur_interval)
            else:
                final_ans.append(cur_interval)

        return final_ans


        