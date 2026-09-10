class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort()
        used = [False] * len(nums)
        def back(start, current_sum, groups):
            if groups == 1:
                return True
            if current_sum == target:
                return back(0, 0, groups - 1)
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if current_sum + nums[i] > target:
                    continue
                if i > start and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                if back(i + 1, current_sum + nums[i], groups):
                    return True
                used[i] = False
            return False
        return back(0, 0, k)    
        