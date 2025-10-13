# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''

[0, 1, 2, 3, 0, 4, 5, 0]



[0, 1, 2, 3, 4, 5, 0]
[15]
cum = 1 + 2 + 3 + 4 + 5


[0, 0]
[]

-> Start with a pointer on the second element of the list
-> if it is not a zero, "Incorporate" the following element and skip / delete through moving the pointer
-> If it is a zero, "skip" / delete through moving the pointer

Time O(N), Space -> O(1)

'''


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        cur = head.next
        cur.next = head.next.next
        while cur:
            # [1, 2, 3, 0, 4, 5, 0]

            if not cur.next.val:
                cur.next = cur.next.next
                cur = cur.next

            else:
                while cur.next.val:
                    cur.val += cur.next.val
                    cur.next = cur.next.next # Deleting next node from the list

        return head.next
                    
        