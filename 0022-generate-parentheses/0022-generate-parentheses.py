class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def ans(open,close,s):
            if open==n and close==n:
                res.append(s)
                return
            if open < n:
                ans(open+1,close,s+"(")
            if close < open:
                ans(open,close+1,s+")")
        ans(0,0,"")
        return res
        
        