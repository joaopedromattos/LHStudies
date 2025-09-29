# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Node:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# class Solution:
    
#     def isLeaf(self, node):
#         return node.left == node.right == None
    
#     def pathSum(self, root:Node, targetSum:int) -> List[List[int]]:
        
#         def dfs(cur:Node, accumSum:int):
            
#             if accumSum + cur.val == targetSum:
#                 if self.isLeaf(cur):
#                     return [cur.val]

#             if self.isLeaf(cur):
#                 return None
            
#             else:
#                 left_result, right_result = None, None
                
#                 if cur.left:
#                     left_result = dfs(cur.left, accumSum=accumSum + cur.val)
                    
#                 if cur.right:
#                     right_result = dfs(cur.right, accumSum=accumSum + cur.val)
                    
#                 return [cur.val, *left_result] if left_result else None, [cur.val, *right_result] if right_result else None
            
#         return dfs(root, accumSum=0)
        
        


class Solution:
    
    def isLeaf(self, node):
        return node.left == node.right == None
    
    def pathSum(self, root:Node, targetSum:int) -> List[List[int]]:
        if not root:
            return []

        if root.val == targetSum:
            if self.isLeaf(root):
                return [[root.val]]
        
        def dfs(cur:Node, accumSum:int):
            
            if accumSum + cur.val == targetSum:
                if self.isLeaf(cur):
                    return [[cur.val]]

            if self.isLeaf(cur):
                return []
            
            else:
                left_result, right_result = [], []
                
                if cur.left:
                    left_result = dfs(cur.left, accumSum=accumSum + cur.val)
                    
                if cur.right:
                    right_result = dfs(cur.right, accumSum=accumSum + cur.val)
              
                paths = []

                if right_result:
                    for path in right_result:
                        paths.append([cur.val] + path)

                if left_result:
                    for path in left_result:
                        paths.append([cur.val] + path)

                return paths
            
        return dfs(root, 0)
        
        