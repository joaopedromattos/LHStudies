'''

In: root (TreeNode)
Out: List

            1
    2               3
4                         5

Out: [4, 2, 1, 3, 5]

Out: [4, 2, <none>. 1, <none>, 3, 5] (In practice)

Principle: (Induction) Node i-th is the parent of node i+1-th. If node i+1-th is on the left, it appears first, if it is on the right, it appears last.

Algo:
-> Call to the left
-> Append to the list
-> Call to the right

Time: O(N) (N=number of nodes in the tree)
Space: O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        inorder = []

        if not root:
            return inorder

        def _isLeaf(node):
            return node.left == node.right == None

        def traversal(node):
            nonlocal inorder

            if _isLeaf(node):
                inorder.append(node.val)
                return

            if node.left:
                traversal(node.left)

            inorder.append(node.val)

            if node.right:
                traversal(node.right)

            return

        traversal(root)
        
        return inorder

