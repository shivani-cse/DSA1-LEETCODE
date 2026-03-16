class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()

        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

                size = 1
                while True:
                    if i + 2*size >= m or j - size < 0 or j + size >= n:
                        break

                    total = 0
                    x, y = i, j
                    for k in range(size):
                        total += grid[x+k][y-k]
                    for k in range(size):
                        total += grid[x+size+k][y-size+k]
                    for k in range(size):
                        total += grid[x+2*size-k][y+k]
                    for k in range(size):
                        total += grid[x+size-k][y+size-k]

                    sums.add(total)
                    size += 1
        return sorted(sums, reverse=True)[:3]    