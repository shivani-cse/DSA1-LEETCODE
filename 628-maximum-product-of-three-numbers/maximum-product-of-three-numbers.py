class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        max_product = nums[-1] * nums[-2] * nums[-3]
        max_product = max(
            max_product,
            nums[0] * nums[1] * nums[-1]
        )

        return max_product