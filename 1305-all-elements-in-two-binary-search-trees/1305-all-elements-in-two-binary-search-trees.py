# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: List[int]
        """
        
        def inorder(root):
            ans=[]
            def dfs(root):
                if root ==None:
                    return      
                dfs(root.left)
                ans.append(root.val)
                dfs(root.right)
            dfs(root)
            return ans

        a=inorder(root1)
        b=inorder(root2)
        i=0
        j=0
        res=[]
        while i < len(a) and j<len(b):
            if a[i]<=b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        while i < len(a):
            res.append(a[i])
            i+=1
        while j < len(b):
            res.append(b[j])
            j+=1
        return res
    
    
        