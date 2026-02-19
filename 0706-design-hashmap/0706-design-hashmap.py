'''

-> All operations in O(1)
-> how many items on average?
-> What should happen when we try to remove an item not present in the hash?
-> In this exercise, are considering universal hash functions? 
-> What if the key already exists? 

hashtable = [_ ...... _] % prime_number % len(hashtable) 

get


put

remove

'''


HASHTABLESIZE=100_000_000
class MyHashMap:
    '''
    naive hash table
    '''

    def __init__(self):
        self.hashmap = [None] * HASHTABLESIZE
        

    def hashfn(self, key) -> Int:
        return (key) % HASHTABLESIZE

    def put(self, key: int, value: int) -> None:
        '''O(1) amortized, o(N) ~adversarial case'''


        idx = self.hashfn(key)
        if self.hashmap[idx]:
            if self.hashmap[idx][0] == key:
                # if the key already exists, update
                self.hashmap[idx % HASHTABLESIZE] = (key, value)
                return None

            # linear probing:
            while self.hashmap[idx % HASHTABLESIZE]:
                idx += 1

        self.hashmap[idx % HASHTABLESIZE] = (key, value)
        # print(self.hashmap)
        return None
        

    def get(self, key: int) -> int:

        idx = self.hashfn(key)
        if self.hashmap[idx]:
            if self.hashmap[idx][0] != key:
                # linear probing:
                while self.hashmap[idx % HASHTABLESIZE] and self.hashmap[idx % HASHTABLESIZE][0] != key:
                    idx += 1

                if not self.hashmap[idx]:
                    return -1


                if self.hashmap[idx][0] == key:
                    return self.hashmap[idx][1]
            else:
                return self.hashmap[idx][1]
        else:
            return -1
        # print(self.hashmap)

    def remove(self, key: int) -> None:
        idx = self.hashfn(key)
        if self.hashmap[idx]:
            if self.hashmap[idx][0] != key:
                # linear probing:
                while self.hashmap[idx % HASHTABLESIZE] and self.hashmap[idx % HASHTABLESIZE][0] != key:
                    idx += 1

                if self.hashmap[idx]:
                    # raise KeyError
                    return None


                if self.hashmap[idx][0] == key:
                    self.hashmap[idx] = None
            else:
                self.hashmap[idx] = None
                return None
        else:
            return None

        # print(self.hashmap)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)