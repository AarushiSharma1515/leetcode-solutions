class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maxocc=0
        while left<right:
            new=(right-left) * min(height[left],height[right])
            maxocc=max(maxocc,new)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxocc