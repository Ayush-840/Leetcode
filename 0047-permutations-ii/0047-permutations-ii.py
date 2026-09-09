class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        path=[]
        nums.sort()
        used=[False]*len(nums)
        def back():
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i >0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i]=True
                back()
                used[i]=False
                path.pop()
        back()
        return ans
        