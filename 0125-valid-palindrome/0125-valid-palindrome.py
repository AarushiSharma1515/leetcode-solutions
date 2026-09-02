class Solution(object):
    def isPalindrome(self, s):
        strs="".join(char for char in s if char.isalnum()).lower()
        left=0
        right=len(strs)-1
        while left<right:
            if strs[left]!=strs[right]:
                return False                
            left+=1
            right-=1
        return True