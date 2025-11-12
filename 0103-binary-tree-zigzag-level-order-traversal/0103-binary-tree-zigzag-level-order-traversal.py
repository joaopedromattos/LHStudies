'''
In: root (TreeNode)

Q for the interviewer: do we start as left or right?

[3, 2, 1, 6, 5, 4]
[[3], [1, 2], [6, 5, 4]]

Principle: Induction -> We need that the i-th node to be included before the i+i-th. Pre-order principle.

N -> Number of nodes
Time: O(n) -> Go over the entire tree
Space: O(N) -> We cannot avoid storing the entire tree to output.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        zz = []

        if not root:
            return zz

        def _isLeaf(node):
            return node.right == node.left == None
        
        def traversal(node, tree_level):
            nonlocal zz

            if len(zz) <= tree_level:
                zz.append(deque([]))

            if tree_level % 2 == 0:
                zz[tree_level].append(node.val)
            else:
                zz[tree_level].appendleft(node.val)

            if _isLeaf(node):
                return

            # Always traverse children left -> right (DON'T swap based on level)
            if node.left:
                traversal(node.left, tree_level + 1)
            if node.right:
                traversal(node.right, tree_level + 1)
            return

        traversal(root, 0)

        return [list(i) for i in zz]
        