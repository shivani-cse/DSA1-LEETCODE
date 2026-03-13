class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes):
        
        def can(t):
            total = 0
            for w in workerTimes:
                x = int(((-1 + (1 + 8*t/w)**0.5) // 2))
                total += x
                if total >= mountainHeight:
                    return True
            return False
        
        left = 1
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        
        return left