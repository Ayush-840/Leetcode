class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        nums.sort()
        def backtarck(i):
            ans.append(path[:])
            for ch in range(i,len(nums)):
                if ch>i and nums[ch]==nums[ch-1]:
                    continue
                path.append(nums[ch])
                backtarck(ch+1)
                path.pop()
        backtarck(0)
        return ans

        