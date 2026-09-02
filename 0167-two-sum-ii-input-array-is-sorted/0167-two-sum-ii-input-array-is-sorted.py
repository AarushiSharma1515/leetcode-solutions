class Solution(object):
    def twoSum(self, numbers, target):
        hashset={}
        for i in range(len(numbers)):
            num1=target-numbers[i]
            if num1 in hashset:
                return [hashset[num1],i+1]
            else:
                hashset[numbers[i]]=i+1
                
