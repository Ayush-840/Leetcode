# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        ans=[]
        def ans1(root):
            if root==None:
                return 
            ans1(root.left)
            ans.append(root.val)
            ans1(root.right)
        ans1(root)
        sum1=0
        for i in ans:
            if low <= i <= high:
                sum1+=i
        return sum1
    
            
        