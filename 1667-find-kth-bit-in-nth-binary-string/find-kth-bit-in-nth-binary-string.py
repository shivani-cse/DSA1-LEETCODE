class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        
        mid = 2**(n-1)  # middle index in 1-indexed string
        
        if k == mid:
            return '1'
        elif k < mid:
            # First half: recurse on Sn-1
            return self.findKthBit(n-1, k)
        else:
            # Second half: mirrored position in first half, then invert
            mirror_pos = 2**n - k
            bit = self.findKthBit(n-1, mirror_pos)
            return '1' if bit == '0' else '0'