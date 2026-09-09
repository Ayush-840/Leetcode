class Solution(object):
    def permute(self, nums):
        ans = []
        path = []
        used = [False] * len(nums)
        def back():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                back()
                used[i] = False
                path.pop()
        back()
        return ans      
        