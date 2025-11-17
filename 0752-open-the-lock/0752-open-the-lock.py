'''
In: List[str] (Deadends), str: target
out: int -> min number of movements

Q -> Can I spin backquards? 

Test

0000 -> start, 0004, deadends = [] -> 4

0000 -> start, 0004, deadends = [0003]
0001 - 0002 - 0012 - 0013 - 0014 - 0004 - 5

Principle: every state as a node -> every valid transition as an edge. moving states => costs one movement


BFS -> Breadth first search

Time: If we need to go over every state -> 10 ** 4 -> 10000 (Super quick)
Space: O(V + E) (Worst case)
'''


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)

        dist = dict() # Maps distance between start and curr state
        dist['0000'] = 0
        explore = deque([('0000', 0)])

        if '0000' in deadends:
            return -1

        while explore: 
            cur_state, cost = explore.popleft()

            # Since all edges have the same weight,
            # the first path that arrives at the target, 
            # means arriving with the smallest path.
            if cur_state == target:
                return cost

            for i in range(4): # wheels
                for direction in [-1, 1]:
                    cur_state_list = list(cur_state)
                    cur_state_list[i] = str( (int(cur_state_list[i]) + direction) % 10)
                    next_state = ''.join(cur_state_list)

                    if next_state not in dist and next_state not in deadends:
                        dist[next_state] = cost + 1
                        explore.append((next_state, cost + 1))

        if target in dist:
            return dist[target]
        else:
            return -1

        