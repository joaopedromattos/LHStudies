'''
In: h => How long does it take until the guards come back, piles -> List[Ints]


- Are the banana piles in order?
- How many hours are we talking about?

1. how long does it take to eat all bananas at k bananas / hour ? (Problem 1)
    - eating in the most optimal way => "priority queue"
    piles = [1, 2, 3, 4, 5], k=3
    piles = [1, 2, 3, 4, 2]
    piles = [1, 2, 3, 1, 2]
    piles = [1, 2, 0, 1, 2]
    ...
    piles = [0, 0, 0, 0, ]
2. What's the minimum value of k to eat all bananas ? (Problem 2) -> A binary search problem. |000......00011111111|


O(n log ^2 n), Space O(piles)


'''


class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        bananas = [-pile for pile in piles]
        heapq.heapify(bananas)

        def can_eat_all_bananas(k, h):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k

                if hours > h:
                    return False

            return True    


        # print(can_eat_all_bananas(11, 5))


        l, h = 0, 1000000000


        while h - l > 1:
            k = (h + l) // 2

            if can_eat_all_bananas(k, hours):
                h = k
            else:
                l = k

        return h

                
            

        