class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        cur = colors[0]
        dist = None

        for i in range(len(colors) - 1, 0, -1):
            if colors[i] != cur:
                dist = i
                break
        
        cur = colors[len(colors) - 1]

        for i in range(len(colors) - 1):
            if colors[i] != cur:
                dist = max(dist, len(colors) - 1 - i)

        return dist
        