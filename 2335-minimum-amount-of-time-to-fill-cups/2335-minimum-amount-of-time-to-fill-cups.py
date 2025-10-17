'''
Ins: amount => list[int]
output: int => secs "Trips"

Ex:
[1, 2, 3]

c, w
w, h
h
h

h, w
h, w,
h, c


Ex: 
[1, 2, 1000]:

h, w
h, w,
h, c
h -|
h   |
h   |
.   |
.   |- 997 calls + 3 => 1000 (minimum possible)
.   |
h_|


c, w
h, w
h -|
h   |
h   |
.   |
.   |- 999 calls + 2-> 1001
.   |
h_|

[5, 4, 4]
c, w [4, 3, 4]
c, w [3, 2, 4]
c, h [2, 2, 3]
c, h [1, 2, 2]
c, h [0, 2, 1]
w, h [0, 1, 0]
w


Principle: 
- Combine trips with the most requested water types, and readjust as you go.
    - Every water cup is like a priority queue
        - At a given timestamp t: take cups with highest "backlog" to prevent single wataer type accumulation at the end.
        - Every time the water cup is carried, diminish priority.


Time: O(M) -> M the water cup type in highest demand.
Space: O(1) -> water cups space


c > w > h:
    amount[0] -= 1 
    amount[1] -= 1
c > h > w:
    amount[0] -= 1 
    amount[2] -= 1

w > c > h:
    amount[1] -= 1 
    amount[0] -= 1
w > h > c:
    amount[1] -= 1 
    amount[2] -= 1

h > w > c:
    amount[2] -= 1 
    amount[1] -= 1
h > c > w:
    amount[2] -= 1
    amount[0] -= 1



if not c

if not w

if not h



'''

# [3, 2, 1]
# m1 = 3, m2 = 3

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        def get_trip(amt):
            max_value_1, max_value_2 = -inf, -inf
            max_1, max_2 = 0, 0
            print("AMT RECEIVED", amt)
            for idx, cur_i in enumerate(amt):
                if cur_i >= max_value_1:
                    max_value_2 = max_value_1
                    max_2 = max_1

                    max_value_1 = cur_i
                    max_1 = idx
                
                if cur_i > max_value_2 and cur_i < max_value_1:
                    max_value_2 = cur_i
                    max_2 = idx
            print(max_1, max_2)
            amt[max_1] = max(amt[max_1] - 1, 0)
            amt[max_2] = max(amt[max_2] - 1, 0)
            return amt
            
        trips = 0
        c, w, h = amount
        while c or w or h:
            c, w, h = get_trip([c, w, h])
            print("Waters", c, w, h)
            trips += 1

        return trips


        