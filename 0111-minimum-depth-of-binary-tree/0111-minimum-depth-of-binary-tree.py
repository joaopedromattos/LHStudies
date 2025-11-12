'''
In: root (TreeNode)
Out: int : min depth of the binary tree 

BFS:
Principle: "For every level of the tree, what's the level in which the shortest branch ends?" 
    Induction: For every node of level i, I check if they are leaf. If at least one of them is leaf, return i

[3, 1, 2, 4, 5,]
s: 3 (leaf ?) No -> level 1
e: 1, 2

s: 1 (leaf ?) no -> level 2
e: 2, 4, 5 

s: 2 (leaf ?) YES -> return 2
e: 4, 5


Time: O(N) -> N number of nodes in the tree
Space: O(L) -> Number of nodes in l-th level


ANOTHER SOLUTION:
DFS:
Compute all paths and return the shortest one
Time: O(N) -> N number of nodes in the tree
Space: O(L) -> Number of nodes in LONGEST PATH

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def _isLeaf(node: TreeNode):
            return node.left == node.right == None

        def measure_length(node, val):
            if _isLeaf(node):
                return val

            right = inf
            if node.right:
                right = measure_length(node.right, val + 1)
            
            left = inf
            if node.left:
                left = measure_length(node.left, val + 1)

            return min(left, right)

        return measure_length(root, 1)



        