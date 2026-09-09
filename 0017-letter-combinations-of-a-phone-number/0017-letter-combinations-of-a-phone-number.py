class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        ans=[]
        path=[]
        phone={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def back(i):
            if i==len(digits):
                ans.append("".join(path))
                return
            for ch in phone[digits[i]]:
                path.append(ch)
                back(i+1)
                path.pop()
        back(0)
        return ans

        