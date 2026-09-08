class Solution(object):
    def combinationSum2(self, candidates, target):
        ans = []
        path = []
        candidates.sort()
        def back(start, target):
            if target == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                # duplicate skip
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                back(i + 1, target - candidates[i])
                path.pop()
        back(0, target)
        return ans

        