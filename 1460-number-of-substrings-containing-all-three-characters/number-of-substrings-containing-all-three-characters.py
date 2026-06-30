class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last={'a':-1,'b':-1,'c':-1}
        ans=0
        for i,ch in enumerate(s):
            last[ch]=i
            earliest=min(last['a'],last['b'],last['c'])
            if earliest>=0:
                ans+=(earliest+1)
        return ans        

        