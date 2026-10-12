# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        if len(res)==1:
            return True
        ans=True
        for x in range(len(res)-1):
            if res[x] >= res[x+1]:
                ans = False
                break
            elif res[x] <res[x+1]:
                    ans = True
            # else:
            #     ans=False
            #     break
        return ans
                


        