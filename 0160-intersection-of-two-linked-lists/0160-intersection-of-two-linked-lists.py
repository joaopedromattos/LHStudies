# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''Two solutions to the same problem.
The first is a trick, very smart trick, for synching pointers.

Second is a naive solution
'''


'''Trick'''
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         # Dirty trick!
#         a, b = headA, headB
#         while a != b:
#             a = a.next if a else headB
#             b = b.next if b else headA

        
#         return a




'''Original Solution'''
class Solution:

    def getListLength(self, root):
        if not root:
            return 0

        cur = root
        size = 0
        while cur:
            cur = cur.next
            size += 1

        return size


    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None
        
        lenA, lenB = self.getListLength(headA), self.getListLength(headB)

        startA = headA
        startB = headB
        if lenA > lenB:
            print(f"Skipping A - {lenA - lenB}")
            for i in range(lenA - lenB):
                startA = startA.next
        else:
            print(f"Skipping A - {lenA - lenB}")
            for i in range(lenB - lenA):
                startB = startB.next

        curA, curB = startA, startB
        while curA and curB:
            print(curA.val, curB.val, curA == curB, curA.val == curB.val, curA.next == curB.next)
            if curA == curB:
                return curA

            curA = curA.next
            curB = curB.next
        
        return None







        