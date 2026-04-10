class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        res = float('inf')
        for i in d:
            if len(d[i]) >= 3:
                temp = float('inf')
                for j in range(len(d[i]) - 2):
                    
                    k = abs(d[i][j] - d[i][j + 1]) + abs(d[i][j + 1] - d[i][j + 2]) + abs(d[i][j + 2] - d[i][j])
                    temp = min(temp, k)
                res = min(res, temp)
        if res == float('inf'):
            return -1
        return res