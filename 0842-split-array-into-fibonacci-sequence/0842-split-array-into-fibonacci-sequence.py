class Solution(object):
    def splitIntoFibonacci(self, num):
        ans = []
        def back(i):
            if i == len(num):
                return len(ans) >= 3
            current = 0
            for j in range(i, len(num)):
                if j > i and num[i] == "0":
                    break
                current = current * 10 + int(num[j])
                if current > 2147483647:
                    break
                if len(ans) >= 2:
                    if current != ans[-1] + ans[-2]:
                        continue
                ans.append(current)
                if back(j + 1):
                    return True
                ans.pop()
            return False
        back(0)
        return ans      
        