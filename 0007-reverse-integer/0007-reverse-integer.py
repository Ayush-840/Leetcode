class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            digit = x % 10
            x //= 10
            # Check overflow before multiplying by 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
            res = res * 10 + digit
        return res * sign   
        