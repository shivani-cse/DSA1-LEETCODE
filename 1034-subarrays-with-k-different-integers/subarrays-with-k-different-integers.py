class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostk(nums,k):
            l=0
            n=len(nums)
            ans=0
            dici={}
            for r in range(n):
                val=nums[r]
                if val in dici:
                    dici[val]+=1
                else:
                    dici[val]=1
                while(len(dici)>k):
                    lval=nums[l]
                    dici[lval]-=1
                    if dici[lval]==0:
                        dici.pop(lval)
                    l+=1
                ans+=r-l+1
            return ans
        ans=atMostk(nums,k)-atMostk(nums,k-1)
        return ans                    
