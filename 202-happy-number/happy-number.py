class Solution:
    def isHappy(self, n: int) -> bool:
        nt=False
        i=0
        while(i<100):
            sum=0
            while(n!=0):
                d=n%10
                sum+=d*d
                n=n//10
            n=sum
            if(n==1):
                return True
            i+=1
        return nt             