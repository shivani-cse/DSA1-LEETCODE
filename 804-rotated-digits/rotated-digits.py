class Solution:
    def rotatedDigits(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            s=str(i)
            if any(d in "347" for d in s):
                continue
            if any(d in "2569" for d in s):
                count +=1
        return count            