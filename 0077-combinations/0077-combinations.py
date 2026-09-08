class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def back(i):
            if len(path)==k:
                ans.append(path[:])
                return
            if i > n:
                return
            path.append(i)
            back(i+1)
            path.pop()
            back(i+1)
        back(1)
        return ans