'''
In: ListNode (Head)
Out: int

[1, 2, 3, 4, 5], pos=3

[1, 2, 3, 4, 5], pos=1 -> For same input (pos is not passed) we have different outputs

We will have to memorize all pointers we have seen so far. 

Principle: Pigeonhole principle: If you have seen n + 1 unique pointers, and you have stored n unique pointers, then one of them is repeated.

Algo : 
-> read current node
-> if in hash
    return cur_pos

-> else:
    add to hash
-> read next

Time: O(N) Space: O(N)

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cycle_index = 0
        pointers = set()
        cur_pointer = head
        while cur_pointer and not (cur_pointer in pointers):
            pointers.add(cur_pointer)
            cur_pointer = cur_pointer.next
            cycle_index += 1
        
        if not cur_pointer:
            return None
        
        return cur_pointer
        