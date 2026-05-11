class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for x in nums:
            temp=[]
            while x>0:
                temp.append(x%10)
                x//=10
            res.extend(temp[::-1])
        return res        
