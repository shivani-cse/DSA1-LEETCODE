class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        velqoradin = nums
        
        prefixGcd = []
        mx = 0
        
  
        for x in velqoradin:
            mx = max(mx, x)
            prefixGcd.append(math.gcd(x, mx))
        
        # Sort
        prefixGcd.sort()
        
        n = len(prefixGcd)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            ans += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return ans 
        