'''
In: ListNode, ListNode Out: ListNode


- Can this number be negative?
- Can this number be float? 
- Are both numbers the same length? 

Principle: For the i-th number in both lists: 
    val = (listA.val + listB.val) % 10 + carry
    new_carry = val % 10

    carry = 1
    (5 + 6) % 10 + 1 = 2

'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        i, j = l1, l2
        carry = 0
        cur = ListNode()
        head = cur
        while i or j:

            if j:
                j_val = j.val
                j = j.next
            else:
                j_val = 0

            if i:
                i_val = i.val
                i = i.next
            else:
                i_val = 0

            print("i", i_val, 'j', j_val, 'carry', carry)
            
            cur.val = (i_val + j_val + carry) % 10
            carry = (i_val + j_val + carry) // 10

            if i or j:
                cur.next = ListNode()
                cur = cur.next

        if carry > 0:
            cur.next = ListNode(val=carry)


        return head

        