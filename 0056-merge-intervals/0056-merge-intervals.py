class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        ans = []

        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                if intervals[i][1] > end:
                    end = intervals[i][1]
            else:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        ans.append([start, end])
        return ans

        