class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)
        if n>len(s2):
            return False
       
        count1 = {}
        count2 = {}

        for ch in s1:
            count1[ch] = count1.get(ch,0) + 1
        left = 0

        for right in range(len(s2)):
            count2[s2[right]] = count2.get(s2[right],0)+1

            if right-left+1 > n:
                count2[s2[left]]-=1
                if count2[s2[left]]==0:
                    del count2[s2[left]]
                left+=1
            
            if count1 == count2:
                return True
        return False