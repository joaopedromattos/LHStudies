# Condition[k] := k > target
# ['a', 'j', 'y' .....], target = 'c'
#   0.   1.   1.  1

# ['c', 'f'] target = 'a'

# "Smallest greater than target" => "The first '1'"
# Time O(logn) -> Space O(1) (or O(n) if you consider the input space)
# 



class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = -1
        h = len(letters) + 1
        target = ord(target)

        condition = lambda k: k > target

        if not condition(ord(letters[-1])):
            return letters[0]

        while h - l > 1:
            k = (h + l) // 2

            if condition(ord(letters[k])):
                h = k
            else:
                l = k

        return letters[h]