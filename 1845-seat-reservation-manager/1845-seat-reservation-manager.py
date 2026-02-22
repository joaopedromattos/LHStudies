'''

__init__(n : int)

reserve() -> return the smallest seat available

unreserve(seatNumber : int) -> unreserves seatNumber.


number of seats => ~around 10^5.
unreserve the same seat twice ? => this is not going to happen.


Principle: for a reserved seat i, i is the smallest from the {available seats}.
minheap -> reserve() -> fetch the smallest seat -> O(log(n))
        -> unreserve() -> O(n)

bisect -> fetch / insert O(log (n))


'''
import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        min_seat = heapq.heappop(self.seats)
        return min_seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


