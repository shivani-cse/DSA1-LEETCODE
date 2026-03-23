class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        p, s = 1, 0
        for d in map(int, str(n)):
            p *= d
            s += d
        return p - s
        