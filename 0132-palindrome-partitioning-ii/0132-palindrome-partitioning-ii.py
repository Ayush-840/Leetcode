class Solution(object):
    def minCut(self, s):
        dp = [-1] * len(s)
        def back(i):
            if i == len(s):
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = len(s)
            for j in range(i, len(s)):
                part = s[i:j+1]
                if part == part[::-1]:
                    cuts = 1 + back(j + 1)
                    ans = min(ans, cuts)
            dp[i] = ans
            return ans
        return back(0) - 1
        return ans[0]       
        