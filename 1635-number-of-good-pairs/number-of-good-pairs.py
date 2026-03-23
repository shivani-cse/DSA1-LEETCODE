class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(nums.count(x) - 1 for x in nums) // 2