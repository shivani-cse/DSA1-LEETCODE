class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def backtrack(i,curr_xor):
            if i==n:
                return curr_xor
            include=backtrack(i+1,curr_xor^ nums[i])    
            exclude=backtrack(i+1,curr_xor)
            return include+exclude
        return backtrack(0,0)    