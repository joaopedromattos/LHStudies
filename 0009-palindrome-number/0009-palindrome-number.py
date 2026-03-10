'''

In: Int, Out: Bool
- Is the number always postive?
- Is the number always integer?
- If the number is single digit, what do we consider?


Principle: A number is a sequence of divisions and multiplications that have to be simmetrical
    - Pointers or stack

Ex: 121 => 121 / 10 => 12 (remainder 1)
    12 => 12 / 10 => 1 (remainder 2)
    1 => 1 / 10 => 0 (remainder 1)

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x

        if num < 0:
            return False
        
        def num_to_list(x):
            num = []
            while x // 10 > 0:
                num.append(x % 10)

                x = x // 10

                if 0 <= x < 10:
                    # Last iteration before quitting
                    num.append(x % 10)

            return num

        list_num = num_to_list(x)

        return list_num == list_num[::-1]

