# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
# Two pointer approach

1 2 3 -> 2 4 6
1 5 3 -> 3 0 6
5 1 3 -> 1 0 2 6


prev = 6
cur = None -> Finished


---
 
prev = 6
cur = None --> Finished

--- 
prev = None -> NewNode! 1 ----5 -> 6
cur = None -> Finished

Time => O(N), Space => O(1)

'''

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None


        prev, cur = None, head
        while cur:
            # 1. Beginning Carry-on
            if not prev and cur.val > 4:
                # prepend a node
                prev = ListNode()
                prev.val = 1
                prev.next = cur
                head = prev

            # 2. Middle Carry-on
            elif prev and cur.val > 4:
                prev.val += 1

            # 3. No Carry-On
            cur.val = (cur.val * 2) % 10
            prev = cur
            cur = cur.next

        return head
            
        