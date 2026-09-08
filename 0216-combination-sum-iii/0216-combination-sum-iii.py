class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def back(i,k,target):
            if len(path)==k:
                if target==0:
                    ans.append(path[:])
                    return
            if i==10:
                return
            if i <= target:
                path.append(i)
                back(i+1,k,target-i)
                path.pop()
            back(i+1,k,target)
        back(1,k,n)
        return ans

        