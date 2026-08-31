class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        counts = Counter(tiles)
        def backtrack():
            total = 0
            for char in counts:
                if counts[char] > 0:
                    total += 1
                    counts[char] -= 1
                    total += backtrack()
                    counts[char] += 1
            return total

        return backtrack()
        