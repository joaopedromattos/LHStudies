'''

["abcde", "abc", "abcdefg"]

a
    b
        c
            d
                e


["abc", "def", "zxf"]

a
    b
        c

O(Words * Length)


'''



class Solution:
    def __init__(self):
        self.trie = {}

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        def checkIfWordExists(trie, word):
            length = 0
            new_aux = trie
            for c in word:
                if c in new_aux:
                    new_aux = new_aux[c]
                    length += 1
                else:
                    return length

            return length

        aux = self.trie
        for i in strs[0]:
            if not i in aux:
                aux[i] = {}
            aux = aux[i]

        max_prefix = len(strs[0])
        for word in strs[1:]:
            max_prefix = min(max_prefix, checkIfWordExists(self.trie, word))
            if max_prefix == 0:
                return ""

        return strs[0][:max_prefix]


'''
In: List[Str], Out: Str


Principle: Intersection over strings. For every given string i, we can check for "how long" it matches *any* other string in a set.
    - By induction, the intersection of one against all, is the intersection of all


'abcd', 'ab', 'bc', "abc"

abcd => abc, bc

potential_len = 4

abcd, abc, potential_len=3

abcd, ab = potential_len=2

abcd, bc = potential_len = 0

return ""



'''





class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        blueprint = strs[0]

        potential_len = len(blueprint)

        for cur_str in strs[1:]:
            cur_potential_len = 0
            while cur_potential_len < len(cur_str) and cur_potential_len < len(blueprint):
                # Counts until when prefix(blue_print) matches prefix(cur_str)
                if cur_str[cur_potential_len] == blueprint[cur_potential_len]:
                    cur_potential_len += 1
                else:
                    break

            potential_len = min(potential_len, cur_potential_len)

        return strs[0][:potential_len]

            

        

