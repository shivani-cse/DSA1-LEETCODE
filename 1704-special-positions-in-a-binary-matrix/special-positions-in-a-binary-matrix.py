#from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        m = len(mat)        # rows
        n = len(mat[0])     # columns
        
        row_count = [0] * m
        col_count = [0] * n
        
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        special = 0
        
    
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        
        return special