class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def check_overlap(last_s, last_e, cur_s, cur_e):
            overlap = False
            if cur_s <= last_s:
                last_s = cur_s
                overlap = True
                

            if cur_e >= last_e and cur_s <= last_e:
                last_e = cur_e
                overlap = True

            if cur_e <= last_e:
                last_e = last_e
                overlap = True

            return overlap, last_s, last_e

        intervals.sort(key=lambda x: x[0])

        s, e = [intervals[0][0]], [intervals[0][1]]
        for cur_s, cur_e in intervals[1:]:
                
            overlap, new_start, new_end = check_overlap(s[-1], e[-1], cur_s, cur_e)

            if overlap:
                s[-1], e[-1] = new_start, new_end
            else:
                s.append(cur_s)
                e.append(cur_e)

        return list(zip(s, e))