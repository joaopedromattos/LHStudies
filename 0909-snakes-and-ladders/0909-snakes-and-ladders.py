'''
In: board List[List[Int]]
Out: min number of dice rolls (until the end)

Q: Is it MANDATORY to take the ladder or to take the snake? 

[[-1 -1],[-1, -1]] -> 1 dice row.

Principle: Given a position i, there are 6 choices. Greedy works, since the cost of each is the same (1 dice row). Take the one that takes you farther.

BFS

Time: O(N + N * 6) => N = number of elements in the board (rows*cols), 6 * N => Number of edges per entry.
Space: O(N) - Considering the inputsize (because we have to store the board regardless)


'''

from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        flip = False
        new_board = []
        for i in range(len(board) - 1, -1, -1):
            row = board[i]
            new_board.extend(list(reversed(row)) if flip else row)
            flip = not flip

        dices = dict()
        dices[0] = 0

        explore = deque([(0, 0)])

        while explore:
            pos, cur_dices = explore.popleft()
            print(pos, dices)

            for i in range(1, 7):
                next_pos = min(pos + i, len(new_board) - 1)

                if new_board[next_pos] != -1:
                    next_pos = new_board[next_pos] - 1

                # print(next_pos)

                if next_pos not in dices or cur_dices + 1 < dices[next_pos]:
                    dices[next_pos] = cur_dices + 1
                    explore.append((next_pos, cur_dices + 1))

        if (len(new_board) - 1) in dices:
            return dices[len(new_board) - 1]
        else:
            return -1
        