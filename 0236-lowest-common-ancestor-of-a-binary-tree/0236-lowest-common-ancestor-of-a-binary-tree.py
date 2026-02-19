'''
In: TreeNode (root), p : TreeNode, q: TreeNode

-> Are there duplicate nodes in the tree?

[3, 4, 1, 5, 6, 2], p=4, q=6

3 -> 4 -> [3, 4]
3 -> 6 -> [3, 6]


[3, 4, 1, 5, 6, 2], p=5, q=6

3 -> 4 -> [3, 4, 5]
3 -> 6 -> [3, 4, 6]

'Principle: The last i-th node shared between root-node paths of p, and q.

-> Search => "two pointer" list matching

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def search(cur_node, node, path):
            
            if cur_node.val == node.val:
                path.appendleft(cur_node)
                return True

            if cur_node.left:
                if search(cur_node.left, node, path):
                    path.appendleft(cur_node)
                    return True

            if cur_node.right:
                if search(cur_node.right, node, path):
                    path.appendleft(cur_node)
                    return True

            return False

        path_a = deque([])
        search(root, p, path_a)

        path_b = deque([])
        search(root, q, path_b)


        path_a = list(path_a)
        path_b = list(path_b)

       
        ptr = 0

        while ptr < len(path_a) and ptr < len(path_b) and path_a[ptr].val == path_b[ptr].val:
            ptr += 1

        return path_a[ptr - 1]

            


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def search(cur_node, node, path):
            
            if cur_node.val == node.val:
                path.appendleft(cur_node)
                return True

            if cur_node.left:
                if search(cur_node.left, node, path):
                    path.appendleft(cur_node)
                    return True

            if cur_node.right:
                if search(cur_node.right, node, path):
                    path.appendleft(cur_node)
                    return True

            return False

        path_a = deque([])
        search(root, p, path_a)

        path_b = deque([])
        search(root, q, path_b)

       
        ptr = 0

        while ptr < len(path_a) and ptr < len(path_b) and path_a[ptr].val == path_b[ptr].val:
            ptr += 1

        return path_a[ptr - 1]




        