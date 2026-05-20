class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        prefix_cmn_array=[0]*n
        for curr_index in range(n):
            cmn_cnt=0
            for a_index in range(curr_index+1):
                for b_index in range(curr_index+1):
                    if A[a_index] == B[b_index]:
                        cmn_cnt +=1
            prefix_cmn_array[curr_index]=cmn_cnt 
        return prefix_cmn_array    

         