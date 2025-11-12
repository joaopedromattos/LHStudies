'''
In: root (TreeNode)
out: list (pre-order)


Question to the interviewer: Are we leff-first or right first?


Principle: (Induction) If i-th node is i+1-th's node parent, then i-th node will appear before i+1th node.




1
2           4
3       5       6
                    7

[1, 2, 4, 3, 5, 6, 7]


Algo: 
-> Everytime I read a node, append to list
-> Call to right
-> Call to left

Time: O(n) -> Have to go over all nodes in the tree
Space: O(n) -> We HAVE to store the output, which is the size of the tree itself.

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        preorder = []

        if not root:
            return preorder

        def _isLeaf(node):
            return node.right == node.left == None

        def traversal(node:TreeNode):
            nonlocal preorder

            preorder.append(node.val)

            if _isLeaf(node):
                return

            # Flip these two ifs for 'right-first'
            if node.left:
                traversal(node.left)

            if node.right:
                traversal(node.right)

            return

        traversal(root)

        return preorder



        