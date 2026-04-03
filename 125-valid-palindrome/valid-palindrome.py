class Solution:
    def isPalindrome(self, s,left=0,right=None):
        if right is None:
            s="".join(char.lower() for char in s if char.isalnum())
            right=len(s)-1
        if left>=right:
            return True
        if s[left]!=s[right]:
            return False
        return self.isPalindrome(s,left+1,right-1)             
        