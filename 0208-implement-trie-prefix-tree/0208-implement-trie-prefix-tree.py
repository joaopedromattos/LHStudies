from collections import defaultdict

class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        
        cur_trie = self.trie
        for i in range(1, len(word) + 1):
            if not (word[:i] in cur_trie):
                cur_trie[word[:i]] = dict()
            
            cur_trie = cur_trie[word[:i]]

        cur_trie['_exists'] = True

        
    def search(self, word: str) -> bool:
        cur_trie = self.trie
        for i in range(1, len(word) + 1):
            if word[:i] in cur_trie:
                cur_trie = cur_trie[word[:i]]
            else:
                return False

        if '_exists' in cur_trie:
            return True

        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur_trie = self.trie
        for i in range(1, len(prefix) + 1):
            if prefix[:i] in cur_trie:
                cur_trie = cur_trie[prefix[:i]]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)