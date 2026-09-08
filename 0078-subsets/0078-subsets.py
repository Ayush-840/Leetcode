class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        def backtrack(i):
            if i==len(nums):
                ans.append(path[:])
                return
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        backtrack(0)
        return ans
        