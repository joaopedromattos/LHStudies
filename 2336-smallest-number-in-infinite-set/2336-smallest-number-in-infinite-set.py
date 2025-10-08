'''
t=0 - [1, 2, 3, ..., inf] -> popSmallest() -> 1
t=1 - [2, 3, ..., inf] -> popSmallest() -> 2
t=3 - [3, ..., inf] -> popSmallest() -> 3
t=4 - [4, ..., inf] -> addBack(1) -> null
t=4 - [1, 4, ..., inf] -> addBack(1) -> null

t=4 - [1, 4, ..., inf] -> popSmallest() -> 1
t=4 - [4, ..., inf] -> popSmallest() -> 4


[1, 2, 3, 4, ...] -> 1
[2, 3, 4, ...] -> 2
[1, 3, 4, ...] -> addBack(1)



history_of_pops = [1, 2, 3]
minimum_in_set = ___


Actions :

popSmallest() -> Time => O(1) Space => O(1)

addBack() -> Time => O(N), being N the number of previous addbacks 

'''
import bisect
from collections import deque


class SmallestInfiniteSet:

    def __init__(self):
        self.minimum_in_set = 1
        self.cur_minimum = self.minimum_in_set
        self.addBackHistory = []
        

    def popSmallest(self) -> int:

        
        minimum = self.cur_minimum

        if self.addBackHistory:
            self.addBackHistory.remove(self.cur_minimum)
            self.cur_minimum = min(self.addBackHistory) if self.addBackHistory else self.minimum_in_set
        else:
            self.minimum_in_set += 1
            self.cur_minimum = self.minimum_in_set

        return minimum
        

    def addBack(self, num: int) -> None:

        if num < self.minimum_in_set:
            # out of order add back
            if not num in self.addBackHistory:
                self.addBackHistory.append(num)
                self.cur_minimum = min(self.addBackHistory)



# class SmallestInfiniteSet:

#     def __init__(self):
#         self.inf_set = [inf]
#         self.cur_minimum = 1
        

#     def popSmallest(self) -> int:

#         if self.inf_set[0] == inf:
#             minimum = self.cur_minimum
#             self.cur_minimum += 1
#         else:
#             minimum = self.inf_set[0]
#             self.inf_set = self.inf_set[1:] # min element

#         return minimum
        

#     def addBack(self, num: int) -> None:
#         if num < self.cur_minimum:
#             i = bisect.bisect_left(self.inf_set, num)
#             if self.inf_set[i] != num:
#                 self.inf_set.insert(i, num)

#             print(self.inf_set)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)