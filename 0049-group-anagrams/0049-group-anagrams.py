from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ['abc', 'zde', 'bca'] -> {'a':1, 'b':1, 'c':1} -> ['abc']
        string_collection = defaultdict(list)
        for string in strs:
            string_collection[frozenset(Counter(string).items())].append(string)

        return list(string_collection.values())
