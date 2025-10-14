# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''

Case 1
[2,1,3,5,6,4,7]
 A B

2 ---> 1 -----> 3 ------> 5

A : 2 ----> 1

Case 2:
[] -> []

Case 3:
[3, 2]

Time O(N) -> Space O(1)

'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd = head
        even_begin = head.next
        even = even_begin

        while even.next and odd.next:
            print(even.val, odd.val)
            if odd.next:
                odd.next = odd.next.next
                if odd.next:
                    odd = odd.next

            if even.next:
                even.next = even.next.next
                if even.next:
                    even = even.next

        odd.next = even_begin

        return head

        


        