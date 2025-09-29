# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isLeaf(self, node: Optional[TreeNode]):
        return node.left == node.right == None
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        def dfs(cur: Optional[TreeNode], accumSum:int):
            if accumSum + cur.val == targetSum:
                if self._isLeaf(cur):
                    return True
                # else:
                #     return False
                
            if self._isLeaf(cur):
                return False
            else:
                left_result = right_result = False
                if cur.left:
                    left_result = dfs(cur.left, accumSum=accumSum + cur.val)
                    
                if cur.right:
                    right_result = dfs(cur.right, accumSum=accumSum + cur.val)
                
                if left_result or right_result:
                    return True
                else:
                    return False
                
        return dfs(root, accumSum=0)