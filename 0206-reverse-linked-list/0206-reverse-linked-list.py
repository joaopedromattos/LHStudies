# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



'''
  
[1, 2, 3] -> [3, 2, 1]


1 -----> 2 -----> 3

node : 1 --> null
head -> 1

---
node : 2 -> 1 
head -> 2 -----> 1 -----> null

---
node : 3 -> 2
head -> 3 -----> 2 -----> 1 -----> null


# empty list case
[1] -> [1]

node 1:
1 -----> null


Time O(N) -> Space O(N)
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        newList = ListNode()
        newList.val = head.val
        newList.next = None
        curNode = head.next
        while curNode:
            newNode = ListNode()

            newNode.val = curNode.val
            newNode.next = newList

            newList = newNode

            curNode = curNode.next

        return newList

        

