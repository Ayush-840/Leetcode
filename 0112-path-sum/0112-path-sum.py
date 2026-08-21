# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False
        if not root.left and not root.right:
            return targetSum==root.val
        
        remain=targetSum-root.val
        return self.hasPathSum(root.left,remain) or self.hasPathSum(root.right,remain)

        
        
        
        