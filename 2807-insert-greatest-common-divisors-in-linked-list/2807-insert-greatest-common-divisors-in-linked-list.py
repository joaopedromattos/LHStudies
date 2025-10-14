# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Case 1:
In -> [1, 2, 3]
Out -> [1, 1, 2, 1, 3]


In -> [3, 4]
Out -> [3, 1, 4]

Case 2:
In -> [3]
Out -> [3]

1. Computing GCD between prev and cur
2. Iterating over the list (Adding nodes)


GCD: Euclid algo -> Computational complexity is up to debate, but we can establish as O(a) in the worst case.
being "a" the size of the largest number between the numbers we are computing the GCD

We are iterating through the list -> O(N) in which N is the size of the list.

'''
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next or not head:
            return head

        def gcd(a, b):
            while b:
                t = b
                b = a % b
                a = t
            return a

        prev = head
        cur = head.next

        while cur:
            new_node_val = gcd(prev.val, cur.val)

            new_node = ListNode()
            new_node.val = new_node_val
            new_node.next = cur
            prev.next = new_node

            prev = cur
            cur = cur.next

        return head
        