'''
In: preorder = list, inorder = list
Out: root (TreeNode)

preorder = [3, 2, 1, 4], inorder = [1, 2, 3, 4]



            3
        2        4
    1

       x 
[3, 2, 1, 4]
[1, 2, 3, 4]
          x 

[3]

final_tree = [3, 2, 4, 1, none]

Principle: Pre-order -> push. Inorder -> Pop. When pre-order and in-order are the same that means I have reached the end of a branch

Time: O(N) -> N => num nodes
Space: O(N) -> Have to store the tree

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        root = TreeNode(val=preorder[0])
        i, j = 1, 0
        node = root
        stack = [root]

        while i < len(preorder) and j < len(inorder):
            
            new_node=TreeNode()

            new_node.val = preorder[i]

            node = stack[-1]
            # print(node)

            if node.val != inorder[j]:
                node.left = new_node
                stack.append(node.left)
            else:
                # print(stack)
                while stack and stack[-1].val == inorder[j]:
                    # print("Emptying stack", stack[-1].val)
                    node = stack.pop()
                    j += 1

                node.right = new_node
                stack.append(node.right)

            i+=1
           
        return root

            
        