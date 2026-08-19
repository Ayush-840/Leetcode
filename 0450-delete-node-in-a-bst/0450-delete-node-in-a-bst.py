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
        if root==None:
            return None
        if key < root.val:
            root.left=self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left==None:
                return root.right
            if root.right==None:
                return root.left
            
            temp=root.right
            while temp.left:
                temp=temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)
        return root
        