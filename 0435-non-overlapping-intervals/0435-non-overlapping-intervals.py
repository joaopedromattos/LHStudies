'''
Intuition : Given a list of intervals that are "hard to schedule".
Principle : An interval i will have priority over an interval j if i has less duration than j and finishes at the same time.

- Sort intervals by the end.
- Scan intervals and count how many intervals we can fit.
- Compute how many we could not.


'''


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key = lambda x : x[1])
        
        count = 0
        cur_end = -inf
        for s, e in intervals:

            if s >= cur_end:
                # This interval does not overlap.
                count += 1
                cur_end = e

        return len(intervals) - count
        