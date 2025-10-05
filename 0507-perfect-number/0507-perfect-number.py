'''

x = 6 -> 6/3, 6/2, 6/1 -> 3 = 6/2, 2=> 6/3, 1 = 6/6
x -> [1, ..., x/2] -> Time O(N/2), Space = O(N/2) 


24 -> 12 * 2, 8 * 3, 6 * 4, 4 * 6, 3 * 8, 2 * 12, 1 * 24

'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        accum = 0
        for i in range(1, num // 2 + 1):
            if (num % i) == 0:
                other_divisor = num / i
                
                if other_divisor < i:
                    break
                accum += i
                accum += other_divisor
            
        return (accum - num) == num
        