# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        if root.val > key:
            root.left=self.deleteNode(root.left,key)
        if root.val < key:
            root.right = self.deleteNode(root.right,key)
    
        if root.val==key:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = root.right
            while temp.left:
                temp=temp.left
            root.val = temp.val
            root.right=self.deleteNode(root.right,temp.val)
        return root