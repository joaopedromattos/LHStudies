

import heapq

# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

#         maxheap = []

#         events = []
#         for s, e, h in buildings:
#             events.append((s, h))
#             events.append((e, -h))


#         events.sort(key=lambda x: (x[0], x[1]))
#         final_answ = []
#         heapq.heapify(maxheap)
#         cur_height = 0
#         for event_time, event_type in events:
#             # if event_type > 0:
#             #     cur_height = max(event_type, cur_height)
#             #     heappq.heappush(maxheap, -event_type)
            
            
#             # if event_type < 0 and event_type == -cur_height
#             #     cur_height = - heappq.heappop()

#             if event_type > 0:
#                 if event_type > cur_height:
#                     cur_height = event_type
#                     final_answ.append([event_time, cur_height])
#                 else:
#                     heapq.heappush(maxheap, -event_type)
#             else:
#                 if maxheap:
#                     if -event_type == cur_height: # The event that's ending is the heighest building
#                         cur_height = - heapq.heappop(maxheap)
#                         final_answ.append([event_time, cur_height])
#                     else:
#                         # If any other building shorter than the tallest one, we can just remove from heap
#                         maxheap.remove(event_type)
#                         heapq.heapify(maxheap)
                
#                 else:
#                     if -event_type == cur_height: # The event that's ending is the heighest building
#                         cur_height = 0

#                         final_answ.append([event_time, cur_height])

#             print(event_time, event_type, 'event added', event_time, cur_height)

#         return final_answ


import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        maxheap = []

        events = []
        for s, e, h in buildings:
            events.append((s, h))
            events.append((e, -h))


        events.sort(key=lambda x: (x[0], -x[1]))
        final_answ = []
        heapq.heapify(maxheap)
        cur_height = 0
        for event_time, event_type in events:
            if event_type > 0:
                if event_type > cur_height:
                    cur_height = event_type
                    final_answ.append([event_time, cur_height])
                
                heapq.heappush(maxheap, -event_type)
            else:
                if maxheap:
                    if event_type == maxheap[0]:
                        last_building = heapq.heappop(maxheap)

                        if maxheap:
                            if last_building != maxheap[0]:
                                final_answ.append([event_time, -maxheap[0]])
                                cur_height = -maxheap[0]
                        else:
                            cur_height = 0
                            final_answ.append([event_time, cur_height])
                    else:
                        maxheap.remove(event_type)
                        heapq.heapify(maxheap)

                

        return final_answ
                
                    