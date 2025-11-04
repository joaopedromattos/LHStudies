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

class FrequencyTracker:
    def __init__(self):
        self.counter = defaultdict(int)
        self.freq_counter = defaultdict(int)
        
    def add(self, number:int): 
        if self.counter[number]:
            self.freq_counter[self.counter[number]] -= 1
        self.counter[number] += 1
        self.freq_counter[self.counter[number]] += 1
        
    def deleteOne(self, number:int):
        if number in self.counter:
            self.freq_counter[self.counter[number]] -= 1
            self.counter[number] -= 1
            
            if self.counter[number]:
                self.freq_counter[self.counter[number]] += 1
            
            if not self.counter[number]:
                del self.counter[number]
                
    def hasFrequency(self, number:int):
        return self.freq_counter[number] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)