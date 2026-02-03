'''


Attr events : List[(start1, end1), (start2, end2), ...]

start1, end1 < start2, end2
end1 < end2

book() (method)
In: Event = (start, end), Out: Bool (True => no overlap, False => Overlap -- we are not free)


events = [(1, 2), (3, 4), (7,8)], event = (5, 6)
1. Find latest index our event can start AND finish to be stored
2. Check overlap
    If not:
        insert event
        return True
    else:
        return False
        
events = [(7,8)], event = (5, 9) -> Edge case

Time: O(N), Space: O(1)

Binary search: Time O(logN), Space O(1)

'''

class MyCalendar:

    def __init__(self):
        self._events = []

    def _checkOverlap(self, curEvent, newEvent):
        if curEvent[0] <= newEvent[0] and newEvent[0] < curEvent[1]:
            return True

        if curEvent[0] < newEvent[1] and newEvent[1] < curEvent[1]:
            return True


        if newEvent[0] <= curEvent[0] and curEvent[0] < newEvent[1]:
            return True

        if newEvent[0] < curEvent[1] and curEvent[1] < newEvent[1]:
            return True

            

        return False
        

    def book(self, startTime: int, endTime: int) -> bool:
        
        if not self._events:
            self._events.append((startTime, endTime))
            return True

        events = []
        # events = [(1, 2), (3, 4), (7,8)], event = (5, 6)
        # print("ALL EVENTS -- ", self._events)
        for idx, (start, end) in enumerate(self._events):
            overlap = self._checkOverlap((start, end), (startTime, endTime))
            # print(overlap, (start, end), (startTime, endTime))

            if overlap:
                return False

        
            
        self._events.append((startTime, endTime))

        return True


    
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)