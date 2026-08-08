class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) are also not palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # When length is odd, clear the middle digit via reversed_half // 10
        return x == reversed_half or x == reversed_half // 10