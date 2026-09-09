class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        used=[False]*(n+1)
        def back(i):
            if i > n:
                return 1
            cnt=0
            for num in range(1,n+1):
                if used[num]:
                    continue
                if num%i==0 or i%num==0:
                    used[num]=True
                    cnt+=back(i+1)
                    used[num]=False
            return cnt
        
        return back(1)