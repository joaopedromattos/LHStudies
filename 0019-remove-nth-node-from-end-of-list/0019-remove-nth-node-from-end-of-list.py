# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

''' 
# Naive solution

[1, 2, 3, 4], n = 3 
-> Scan list, to get list.length
-> Scan deleting the item
-> O(2 * n)


# "Hacky recursion solution"
-- case 1: removing from the middle / end
-> Recursion until end of the list.
-> Update global variable
-> Take back from the ith == length - n - 1 iteration (previous from the element we want to return)
    -- case 2: removing the first
    - check if your length - n - 1 < 0, then update the head
-> Update that pointer
-> O(n) -> Single pass





'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head

        if not head.next:
            return None

        list_length = 0
        def recursion(cur, i):
            nonlocal list_length, head

            if not cur.next:
                list_length = i + 1
                return

            recursion(cur.next, i + 1)

            print(cur.val, i, list_length, n )


            if list_length - n - 1 < 0:
                # We are trying to remove the first element
                head = cur.next
            

            if i == list_length - n - 1:
                # We are in the correct iteration to update our pointer 
                # cur => element before the one we want to remove
                cur.next = cur.next.next



        recursion(head, 0)
        return head



        