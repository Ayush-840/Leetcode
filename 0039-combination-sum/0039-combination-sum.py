class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def back(i,target):
            if target==0:
                ans.append(path[:])
                return
            if i==len(candidates):
                return
            #take
            if candidates[i]<=target:
                path.append(candidates[i])
                back(i,target-candidates[i])
                path.pop()
            #not take
            back(i+1,target)
        back(0,target)
        return ans


        