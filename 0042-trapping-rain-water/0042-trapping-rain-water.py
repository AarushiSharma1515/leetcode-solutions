class Solution(object):
    def trap(self, height):
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        res=0
        while left<right:
            unit=0
            if height[left]<height[right]:
                if leftmax>height[left]:
                    unit=leftmax-height[left]
                leftmax=max(leftmax,height[left])
                left+=1
            else:  
                if rightmax>height[right]:
                    unit=rightmax-height[right]
                rightmax=max(rightmax,height[right])
                right-=1
            res+=unit
        return res