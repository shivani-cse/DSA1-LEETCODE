class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        l=0
        n=len(answerKey)
        cntt=0
        cntf=0
        for r in range(n):
            if (answerKey[r]=="T"):
                cntt+=1
            else:
                cntf+=1
            while(min(cntt,cntf)>k):
                if (answerKey[l]=="T"):
                    cntt-=1
                else:
                    cntf-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans                