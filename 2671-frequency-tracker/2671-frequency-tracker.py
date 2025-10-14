'''
In: Int
out -> [null, Bool]

['add', 'add', 'hasFrequency']
[3, 2, 1 ]

[null, null, False]


['add', 'add', 'deleteOne', hasFreq]
[3, 2, 2, 2]

[null, null, null, False]
----> If counter[number] == 0 -> update the tracker to say "not present"

Implement as a hash / lookup table

Time / Space (w.r.t. the number of calls)
add -> O(1) / O(1) amortized

deleteOne -> O(1) / O(1) amortized

hasFrequency -> O(n) / O(1) amortized -> N is the number of items in the dictionary

'''

from collections import defaultdict
class FrequencyTracker:

    def __init__(self):
        self.tracker = defaultdict(int)
        self.freq_tracker = defaultdict(set)
        

    def add(self, number: int) -> None:
        if self.tracker[number]:
            self.freq_tracker[self.tracker[number]].remove(number)
        self.tracker[number] += 1
        self.freq_tracker[self.tracker[number]].add(number)
        

    def deleteOne(self, number: int) -> None:
        if number in self.tracker:
            self.freq_tracker[self.tracker[number]].remove(number)
            self.tracker[number] -= 1

            if self.tracker[number]:
                self.freq_tracker[self.tracker[number]].add(number)

            if not self.tracker[number]:
                # Update tracker to say "not present"
                # as soon as we do not have the number anymore.
                del self.tracker[number]
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_tracker[frequency] != set()
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)