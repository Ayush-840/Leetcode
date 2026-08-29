class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        prev1, prev2 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return prev2       