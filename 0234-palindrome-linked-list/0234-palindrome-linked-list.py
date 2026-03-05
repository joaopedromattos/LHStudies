'''




'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        i,j = head, head
        palindrome_check = True
        def go_backwards(j):
            nonlocal i, palindrome_check
            if j.next:
                go_backwards(j.next)
            
            # print(i.val, j.val)
            if i.val != j.val:
                palindrome_check = False
            
            i = i.next
        
        go_backwards(j)

        return palindrome_check
        