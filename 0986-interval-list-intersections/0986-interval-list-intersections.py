'''
In: List[List[int, int]], List[List[int, int]]
Out: List[List[int, int]]

Q: Are the input lists in order? -> yes
Q: Are the lengths of the lists the same? -> no

[[1, 3], [4, 7]], [[1, 2], [3, 7]]


final_output = [[1, 2], [3, 3], [4, 6]]
i, j = 0, 0 => [1, 3] intersection [1, 2] => rule := max(start1, start2), min(end1, end2) [1, 2]
i, j = 0, 1 => [1, 3] intersection [3, 7] => rule := max(start1, start2), min(end1, end2) [3, 3]
i, j = 1, 1 => [4, 6] inter [3, 7] => [max(4, 3), min(6, 7)] => [4, 6]

---
    i                 j
[[1, 3], [4, 6]], [[2, 7]]

            i         j  
[[1, 3], [4, 6]], [[2, 7]]


final_output = [2, 3], [4, 6]

1------3 4------6
   2---3 4----------7

[2, 3], [4, 6]
       

Principle: For each interval, explore interval until it is exhausted, then we go to the next one. Only the current intervals matter. All final outputs will be disjoint by definition.

Time: O(N + M)
Space: O(N + M) N => Length list 1, M => Length list 2.



'''




class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        def get_overlap(interval1, interval2):
            case1 = interval1[0] <= interval2[0] and interval2[0] <= interval1[1]
            case2 = interval1[0] <= interval2[1] and interval2[1] <= interval1[1]
            case3 = interval2[0] <= interval1[0] and interval1[1] <= interval2[1]
            return case1 or case2 or case3


        def get_intersection(interval1, interval2):
            final_intersection = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
            increment_interval_1 = final_intersection[1] == interval1[1]
            return final_intersection, increment_interval_1


        if firstList == [] or secondList == []:
            return []

        final_output = []
        i, j = 0, 0
        n, m = len(firstList), len(secondList)
        while i < n and j < m:
            interval1, interval2 = firstList[i], secondList[j]
            if get_overlap(interval1, interval2):
                intersection, increment_interval_1 = get_intersection(interval1, interval2)
                final_output.append(intersection)

                if increment_interval_1:
                    i += 1
                else:
                    j += 1


            else:
                if interval1[1] < interval2[1]:
                    i += 1
                else:
                    j += 1


        return final_output




        