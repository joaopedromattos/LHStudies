'''

In: root (TreeNode)

Out: list

Principle: (Inductio n) If the node i is parent of the node i+1, then the node i+1 will be finished first than the node i.

-> Important question for the interviewer: Are "left first" or "right first"?
----> Assuming left first for this exercise.

3

2   1

6. 7    5   None
none none none 4 none

# Right-first
[4, 5, 7, 6, 1, 2, 3]

# Left-first
[6, 7, 4]

Time: O(N) -> We have to go over every single node.
Space: O(N) -> We have to store every single node to return

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        postorder = []

        if not root:
            return postorder

        def _isLeaf(node):
            return node.right == node.left == None

        def traverse(node):
            nonlocal postorder

            if _isLeaf(node):
                postorder.append(node.val)
                return


            if node.left:
                traverse(node.left)
            
            if node.right:
                traverse(node.right)

            postorder.append(node.val)
            return

        traverse(root)

        return postorder



        