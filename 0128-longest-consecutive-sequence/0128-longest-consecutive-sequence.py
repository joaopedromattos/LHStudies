"""
In: List[int], Out: Int


Principle: First thing that comes to mind => O(n^2) Brute force.
    - For every given number, check if the the next numbers are in the sequence.
    - Time O(n^2)


    -> However we do not need to check for every element.
        - Just for start of sequences.
        - Do a set:
            - If the number before current one is in the set, we can skip (it is not the beginning of a sequence)
            - If it is not in the set, check if consecutives are.
            - Worst case: we have two huge sequences, one slighly larger than the other
                - [1...1000, 1002, ..., 10_000]
                - O(2 * n)


"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = set(nums)
        max_seq_len = 0
        for num in lookup:
            if num - 1 in lookup:
                continue
            
            seq_len = 1
            next_value = num

            while next_value + 1 in lookup:
                seq_len += 1
                next_value += 1

            max_seq_len = max(seq_len, max_seq_len)
        return max_seq_len