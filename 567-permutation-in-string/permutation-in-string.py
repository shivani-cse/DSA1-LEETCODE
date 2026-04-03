class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1)>len(s2):
            return False


        freq_s1 = Counter(s1)

        freq = {}

        for i,ch in enumerate(s2):
            if i<len(s1):
                freq[ch] = freq.get(ch,0)+1

            else:
                freq[s2[i-len(s1)]] -= 1
                if freq[s2[i-len(s1)]]==0:
                    del freq[s2[i-len(s1)]]
                freq[ch] = freq.get(ch,0)+1
             
            
            if freq_s1==freq:
                return True
        
        return False