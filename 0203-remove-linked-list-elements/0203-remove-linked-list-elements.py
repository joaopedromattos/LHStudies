# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
# Two pointer approach

# Case 1 (Middle)
val = 2
[1, 2, 2, 3, 4]

prev : 1
cur : 2

prev.next = cur.next # Skipping current value
cur = cur.next
[1, 3, 4]

--- 
# case 2 (Beginning)
val = 1
[1, 2, 2, 3, 4]

if not prev:
    head = cur.next

---
# Case 3 (End) (Pretty much same as Case 1)
val = 4
[1, 2, 2, 3, 4]

prev = 3
cur = 4

prev.next = cur.next # Skipping current value
cur = cur.next


Time O(N), Space O(1)
'''


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None        

        prev, cur = None, head

        while cur:

            # Case 2: (Beginning)
            if not prev and cur.val == val:
                head = cur.next

            # Case 1 and 3: cur.val == val
            elif prev and cur.val == val:
                prev.next = cur.next

            else:
                # If we did not update prev,
                # we're just going to move to the right
                prev = cur
                

            cur = cur.next

        return head
        