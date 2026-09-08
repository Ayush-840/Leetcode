class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def back(i,target,nums):
            if target==0:
                ans.append(path[:])
                return
            if i==len(nums):
                return
            if nums[i]<= target:
                path.append(nums[i])
                back(i,target-nums[i],nums)
                path.pop()
            back(i+1,target,nums)
        back(0,target,candidates)
        return ans
