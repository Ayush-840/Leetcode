# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def solve(node,p,q):
            if node is None:
                return None
            if node==p or node==q:
                return node
            left = solve(node.left,p,q)
            right = solve(node.right,p,q)
            if left is None and right is None:
                return None
            elif left is None:
                return right
            elif right is None:
                return left
            return node
        return solve(root,p,q)
        