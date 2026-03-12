from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa == pb:
                return False
            parent[pa] = pb
            return True

        def can(x):
            parent[:] = list(range(n))
            upgrades = 0
            used = 0

            # mandatory edges
            for u, v, s, m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if union(u, v):
                        used += 1
                    else:
                        return False

            optional = []
            for u, v, s, m in edges:
                if m == 0:
                    optional.append((u, v, s))

            optional.sort(key=lambda e: -e[2])

            for u, v, s in optional:
                if used == n - 1:
                    break

                if find(u) != find(v):
                    if s >= x:
                        union(u, v)
                        used += 1
                    elif 2 * s >= x and upgrades < k:
                        union(u, v)
                        upgrades += 1
                        used += 1

            return used == n - 1

        lo, hi = 0, 2 * 10**5
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans