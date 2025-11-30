'''
In: Root 
Out: Root

[1, 2, 3] => [2, 1, 3]

[1, 3, null, 2] => [3, 1, null, 2] => Error happens in two immediate nodes.



Also question for the interviewer: Error always happens in two immediate nodes?
Answer: No.
[4, 1, 3, null, null, 2, 5] => Error in non-immediate nodes.

Principle: For a given node, re-insert in the tree and check if the positions match. The first node to which it fails, it's the node to be swapped.

O(N * Log N) -> If the tree has n nodes
Space (N) -> N is the size of the tree


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

        # def traverseTree(root, node):

        #     if node.val == root.val:
        #         return ...


        #     while ...:
        #         if node.val < root.val:
        #             root = root.left
        #         else:
        #             root = root.right




        # def dfs(node):


        #     # TODO
        #     if node.right
        #         dfs(node.right)


        #     if node.left:
        #         dfs(node.left)



'''


In: root_node
Out: None


Test: 


[4, 1, 5, 0, 6, None, 7]

Flip 6 with 4.

Principle: How to transform this tree into a valid BST. Think of BST as a list -> traverse as in-order.

For a given node
    - Find the "cannonical" / correct position in the BST
    - if it matches
        - go check the next node
    - if it does not
        - swap with the first node that does not respect the BST


O(N)
O(logN)
'''

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def is_leaf(node):
            return node.left == node.right == None


        def check_position(node, val):
            if node.val == val:
                return True

            if val < node.val and node.left:
                return check_position(node.left, val)
            elif val > node.val and node.right:
                return check_position(node.right, val)
            else:
                return False


        def traverse(node):
            if not check_position(root, node.val):
                # we are in the "invalid" node
                return node

            if is_leaf(node):
                return None

            left_tree = None
            if node.left:
                left_tree = traverse(node.left)

            right_tree = None
            if node.right:
                right_tree = traverse(node.right)

            if left_tree != None and node.val < left_tree.val:
                # left_tree is the invalid node
                aux = node.val
                node.val = left_tree.val
                left_tree.val = aux
                return None # already fixed the tree
            
            if right_tree != None and node.val > right_tree.val:
                # right_tree is the invalid node
                aux = node.val
                node.val = right_tree.val
                right_tree.val = aux
                return None # already fixed the tree

            if left_tree:
                return left_tree
            elif right_tree:
                return right_tree
            else:
                return None

        traverse(root)


'''


In: root_node
Out: None


Test: 


[4, 1, 5, 0, 6, None, 7]

Flip 6 with 4.

Principle: How to transform this tree into a valid BST. Think of BST as a list -> traverse as in-order.

For a given node
    - Find the "cannonical" / correct position in the BST
    - if it matches
        - go check the next node
    - if it does not
        - swap with the first node that does not respect the BST


O(N)
O(logN)
'''

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def is_leaf(node):
            return node.left == node.right == None

        first, second, prev = None, None, None
        def traverse(node):
            nonlocal first, second, prev
            if node.left:
                traverse(node.left)

            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node

            prev = node

            if node.right:
                traverse(node.right)

        traverse(root)

        if first and second:
            first.val, second.val = second.val, first.val



            


            
            



                

            

