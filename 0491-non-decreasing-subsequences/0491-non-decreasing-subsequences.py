class Solution(object):
    def findSubsequences(self, nums):
        ans = []
        path = []
        def backtrack(i):
            if len(path) >= 2:
                if path[:] not in ans:
                    ans.append(path[:])
            for j in range(i, len(nums)):
                if path and nums[j] < path[-1]:
                    continue
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return ans