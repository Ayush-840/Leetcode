class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans=[]
        path=[]
        def back(i):
            if i==len(s):
                ans.append(path[:])
                return
            for j in range(i,len(s)):
                part=s[i:j+1]
                if part == part[::-1]:
                    path.append(part)
                    back(j+1)
                    path.pop()
        back(0)
        return ans
        