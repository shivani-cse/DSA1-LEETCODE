class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
       
        res = []
        
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]
            
            m = total % 26
            idx = 25 - m     # reverse mapping
            res.append(chr(ord('a') + idx))
        
        return "".join(res)

       