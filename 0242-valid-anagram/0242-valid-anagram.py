# Or using Python's built-in from collections import Counter()0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # acb = abc
        # aabc != bac
        return self.createCounter(s) == self.createCounter(t)

    def createCounter(self, s:str):
        counter = defaultdict(int)
        for i in s:
            counter[i] += 1

        return counter
        

    