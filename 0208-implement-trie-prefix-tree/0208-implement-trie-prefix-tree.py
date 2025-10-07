class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        cur_trie = self.trie
        for i in word:
            if i not in cur_trie:
                cur_trie[i] = {}
            
            cur_trie = cur_trie[i]

        cur_trie['_exists'] = True
        

    def search(self, word: str) -> bool:
        cur_trie = self.trie
        for i in word:
            if i not in cur_trie:
                return False
            
            cur_trie = cur_trie[i]

        return '_exists' in cur_trie
        

    def startsWith(self, prefix: str) -> bool:
        cur_trie = self.trie
        for i in prefix:
            if i not in cur_trie:
                return False
            
            cur_trie = cur_trie[i]

        return True


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)