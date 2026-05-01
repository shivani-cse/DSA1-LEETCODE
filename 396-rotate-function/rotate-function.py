class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sm = sum(nums)

        start = 0
        cnt = 0
        for i in range(len(nums)):
            start += (nums[i] * cnt)
            cnt += 1
        
        mx = -inf
        for j in range(len(nums) - 1, -1, -1):
            mx = max(mx, start)
            start = start + sm - (len(nums) * nums[j])
        
        return mx