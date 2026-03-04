'''
In: temperatures = List[int], Out: List[Int]

- Are we considering warmer only or equal or warmer?
- What happens if there's no future day that is warmer?


Principle: For every day i there is a day i + 1 that contains our answer.

- One solution : Two pointers:
    - Pointer i is the current day
    - Pointer j is the following day
        - pointer j += 1 until temperature[j] > temperature[i]

-> Worst case: O(n^2) (!!!!!) -> Can get very expensive very fast.


[73,74,75,71,69,72,76,73]

[1, 1, ]

[(71, 3), (69, 4), (72, 5) (76, 6)]


[100, 99, 98,.....1]







'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                j += 1

            if j != len(temperatures):
                ans[i] = j - i

        return ans
        


'''
Second idea:
Sliding stack:
A stack keeps track of days that were not solved yet.


O(n) => every element is popped or pushed only once.

'''



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j

            stack.append(i)
           

        return ans