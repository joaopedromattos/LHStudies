'''

- first int is 0
- every number is unique
- adjacent pairs change by one bit
- first and last differ by only one bit


In: int
out: valid gray code sequence


Test: 
n=3 -> 2 ** n numbers

_ _ _ _ ... _
___n bits___



000 => 001, 010, 100 vis =(000)
001 => 011, 101 vis=(000, 001)
011 => 111, 010, 100 vis = (000, 001, 011)
...
final state: 010, 100


Principle: Navigate through all possible paths, until we find a valid one (there are multiple optimal solutions, so dp does not apply).


Graph -> Adjacent states are bits that are changed. Gray code : 2 ** n / 2 hops

Time: O((n-1) * 2 ** n) (no memoization is possible)
Space: O( N ) -> For every sequence of recursive calls, we just need to store the current path

'''


class Solution:
    def grayCode(self, n: int) -> List[int]:

        def addBitInPosition(number, i):
            return (number + (2 ** i)) % (2 ** n)

        def subtractBitInPosition(number, i):
            return (number - (2 ** i)) % (2 ** n)

        
        single_bit_change = lambda result: (result > 0) and ((result & (result - 1)) == 0)

        def isGrey(cur_code):
            return cur_code[0] == 0 and single_bit_change(cur_code[0] ^ cur_code[-1]) # rule: first has to be zero, last and first have to differ by a bit only

        final_grey_code = None
        def bt(state: int, cur_code, visited):
            nonlocal final_grey_code
            # base case:
            if len(cur_code) == 2 ** n: # rule: 2 ** n elements
                if isGrey(cur_code):
                    final_grey_code = cur_code
                    return True
                else:
                    return False

            for i in range(n):
                for ops in ('add', 'sub'):
                    # rule: only 1 bit difference
                    if ops == 'add':
                        next_state = addBitInPosition(state, i) 
                    else:
                        next_state = subtractBitInPosition(state, i)
                    if (not next_state in visited) and single_bit_change(state ^ next_state): # rule: cannot repeat numbers
                        # print(bin(state), bin(next_state), cur_code)
                        cur_code.append(next_state)
                        visited.add(next_state)
                        grey_code_found = bt(next_state, cur_code, visited)
                        if grey_code_found:
                            return True
                        cur_code.pop()
                        visited.remove(next_state)

        bt(0, [0], set([0]))
        
        return final_grey_code        