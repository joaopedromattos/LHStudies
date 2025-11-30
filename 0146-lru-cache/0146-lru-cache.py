'''

- get()
    In: key (int)
    Out: val (int)

    Hashmaps / hashsets
    
    Test: 

    [(1:2), (3:2), (4:3)]
    get(1) -> 2 Time O(1) / Space O(capacity)

- put()
    - In: key (int), val (int)
    - out: none

    
    [4:5, 3:4, 2:5, 1:6]

    - is miss>? O(1) / O(capacity)
        if yes:
            pop last node
            add new node
            counter = 1
        else:    
            - Check for swapping


    

A -> B -> C

A-------->C 
    B ----> C


'''

class Node:
    def __init__(self, key= None, val= None, next_node= None, prev_node=None):
        self.key = key
        self.val = val
        self.next = next_node
        self.prev = prev_node


class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove_node(node)
            self.insert_at_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.remove_node(node)
            self.insert_at_head(node)
        else:
            # Cache miss
            
            # Check if the least used is in the lookup
            if len(self.lookup) == self.capacity:
                prev = self.tail.prev
                self.remove_node(prev)
                del self.lookup[prev.key]

            new_node = Node(key, value)
            self.lookup[key] = new_node
            self.insert_at_head(new_node)


            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)