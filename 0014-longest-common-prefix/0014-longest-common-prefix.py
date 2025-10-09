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
        aux['_'] = True

        max_prefix = len(strs[0])
        for word in strs[1:]:
            max_prefix = min(max_prefix, checkIfWordExists(self.trie, word))
            if max_prefix == 0:
                return ""

        return strs[0][:max_prefix]
            

        

