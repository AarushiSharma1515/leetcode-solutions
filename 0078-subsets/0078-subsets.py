class Solution(object):
    def subsets(self, nums):
        outputs = []
        def backtrack(start , path):
            outputs.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1 , path)
                path.pop()
        backtrack(0,[])
        return outputs