class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
       
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        for i in range(n):
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""

        s = [''] * n
        ch = 'a'

        for i in range(n):
            if s[i] == '':
                if ch > 'z':
                    return ""
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        s[j] = ch
                ch = chr(ord(ch) + 1)

        s = ''.join(s)

        dp = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s[j]:
                    if i == n-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i+1][j+1]

        return s if dp == lcp else ""