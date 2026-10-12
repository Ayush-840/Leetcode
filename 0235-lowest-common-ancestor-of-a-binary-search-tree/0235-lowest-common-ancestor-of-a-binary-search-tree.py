# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root



        