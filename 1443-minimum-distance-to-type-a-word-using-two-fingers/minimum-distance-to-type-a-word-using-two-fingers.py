class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def dist(c1, c2):
            if c1 is None or c2 is None:
                return 0
            
            x1, y1 = divmod(ord(c1) - ord('A'), 6)
            x2, y2 = divmod(ord(c2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        
        dp = {}
        
        def solve(pos, f1, f2):
            
            if pos == n:
                return 0
            
            if (pos, f1, f2) in dp:
                return dp[(pos, f1, f2)]
            
            curr = word[pos]
            
           
            cost1 = float('inf')
            if f1 == -1:
                cost1 = solve(pos + 1, pos, f2)
            else:
                cost1 = dist(word[f1], curr) + solve(pos + 1, pos, f2)
            
            cost2 = float('inf')
            if f2 == -1:
                cost2 = solve(pos + 1, f1, pos)
            else:
                cost2 = dist(word[f2], curr) + solve(pos + 1, f1, pos)
            
            dp[(pos, f1, f2)] = min(cost1, cost2)
            return dp[(pos, f1, f2)]
        
        return solve(0, -1, -1)