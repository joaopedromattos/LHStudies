'''
In: begin : str, end : str, wordList : List[str]

Q: Can I only go from i to i+1, right?

begin : abc - end : dfc - [abc, dbc, dfc]


"hit" -> "h*t", "*it", "hi*"
        


'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def generateWildcards(word):
            list_chars = list(word)
            wildcards = []
            for i in range(len(word)):
                aux = list_chars[i]
                list_chars[i] = '*'
                wildcards.append(''.join(list_chars))
                list_chars[i] = aux
            return wildcards

        def createSet(wordList):
            wordLookup = dict()
            for word in wordList:
                for wildcard in generateWildcards(word):
                    if wildcard not in wordLookup:
                        wordLookup[wildcard] = set()

                    wordLookup[wildcard].add(word)

            return wordLookup


        wildcard_set = createSet(wordList)

        dist = dict()
        dist[beginWord] = 1
        to_explore = deque([(1, beginWord)])

        while to_explore:

            cur_dist, cur_word = to_explore.popleft()
            # print(cur_dist, cur_word)

            if cur_word == endWord:
                return cur_dist

            for cur_wildcard in generateWildcards(cur_word):
                
                if cur_wildcard in wildcard_set:
                    for neighbor_word in wildcard_set[cur_wildcard]:
                        
                        # print(dist, cur_word, cur_wildcard, cur_wildcard in wildcard_set, neighbor_word)
                        if (neighbor_word not in dist):
                            to_explore.append((cur_dist + 1, neighbor_word))
                            dist[neighbor_word] = cur_dist + 1

                        elif cur_dist + 1 < dist[neighbor_word]:
                            to_explore.append((cur_dist + 1, neighbor_word))
                            dist[neighbor_word] = cur_dist + 1

        return 0


                