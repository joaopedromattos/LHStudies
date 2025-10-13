# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''

[1, 2, 3]

cur.val, cur.next.


cur.next.next != None
cur.val = cur.next.val
cur = cur.next

'''

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        cur = node
        while cur.next.next:
            cur.val = cur.next.val
            cur = cur.next

        # `cur` is the second to last element
        cur.val = cur.next.val
        cur.next = None
        