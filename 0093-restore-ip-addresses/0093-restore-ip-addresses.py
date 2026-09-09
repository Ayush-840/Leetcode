class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans=[]
        path=[]
        def back(i):
            if len(path)==4:
                if i==len(s):
                    ans.append(".".join(path))
                    return
            for j in range(i, min(i + 3, len(s))):
                part = s[i:j + 1]
                if len(part) > 1 and part[0] == "0":
                    continue
                if int(part) > 255:
                    continue
                path.append(part)
                back(j + 1)
                path.pop()
        back(0)
        return ans
        