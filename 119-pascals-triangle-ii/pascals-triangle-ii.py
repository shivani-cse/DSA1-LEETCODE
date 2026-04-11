class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr,ans=1,[1]
        for i in range(1,rowIndex+1):
            curr=curr*(rowIndex+1-i)//i
            ans.append(curr)
        return ans    