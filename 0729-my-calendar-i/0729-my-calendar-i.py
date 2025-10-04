'''
[[10, 15], [20, 25]] -> book([11, 16]) 

--- 

[[10, 15], [20, 25], [11, 16]] -> sort(key=start_time)
[[10, 15], [11, 16], [20, 25]] -> double_booking=True


Time : O(N + NlogN) Space : O(N) (Not considering the original events) / O(2 * N) (Considering the original events)

'''



class MyCalendar:

    def __init__(self):
        self.events = []

    
    def _doubleBooking(self, event:List):
        events_clone = self.events[:]

        events_clone.append(event)

        events_clone.sort(key=lambda x: x[0])

        s, e = [events_clone[0][0]], [events_clone[0][1]]
        for cur_start, cur_end in events_clone[1:]:

            if cur_start >= s[-1] and cur_start < e[-1]:
                return True
            else:
                s.append(cur_start)
                e.append(cur_end)

        # No conflicts found!
        self.events = events_clone

        return False
            
        
    def book(self, startTime: int, endTime: int) -> bool:
        return not self._doubleBooking(event=[startTime, endTime])
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)