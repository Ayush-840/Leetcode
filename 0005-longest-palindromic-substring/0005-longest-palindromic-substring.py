class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
        start, max_len = 0, 0
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length and starting index of the palindrome found
            return right - left - 1, left + 1
        for i in range(len(s)):
            # Odd length palindromes (e.g. "aba")
            len1, start1 = expand_around_center(i, i)
            # Even length palindromes (e.g. "abba")
            len2, start2 = expand_around_center(i, i + 1)
            if len1 > max_len:
                max_len = len1
                start = start1
            if len2 > max_len:
                max_len = len2
                start = start2
        return s[start : start + max_len]
        