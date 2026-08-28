class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        first_str = strs[0]
        for i, char in enumerate(first_str):
            for other_str in strs[1:]:
                if i == len(other_str) or other_str[i] != char:
                    return first_str[:i]  
        return first_str       

        