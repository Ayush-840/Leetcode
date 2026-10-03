class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '('
                if stack:
                    stack.pop()
                # Push back the reversed substring
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)      