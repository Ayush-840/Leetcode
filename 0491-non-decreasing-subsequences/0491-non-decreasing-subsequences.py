class Solution(object):
    def findSubsequences(self, nums):
        ans = []
        path = []
        def backtrack(i):
            if len(path) >= 2:
                ans.append(path[:])
            used = set()
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                if path and nums[j] < path[-1]:
                    continue
                used.add(nums[j])
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()
        backtrack(0)
        return ans