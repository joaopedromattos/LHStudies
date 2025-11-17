'''
In: "root" [Node]
Out: List

[3, 2, 4, 1, none, none, none]

[[3], [2, 4], [1]]

3, 0


[[3]]

2, 1

[[3], [2]]

4, 1

[[3], [2, 4]]




Principle: Given a node, and its level, store the node into a list of the corresponding level

Time O(N) -> N = number of nodes in the tree
Space O(N) -> We have to store the entire tree to return

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = []

        if not root:
            return []

        def dfs(node, cur_level):
            nonlocal levels

            if not cur_level < len(levels):
                levels.append([])
            
            levels[cur_level].append(node.val)

            if node.left:
                dfs(node.left, cur_level + 1)

            if node.right:
                dfs(node.right, cur_level + 1)

            return

        dfs(root, 0)

        return levels

        

        

        
        