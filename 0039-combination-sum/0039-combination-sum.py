class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(idx,rem,curr):
            if rem==0:
                res.append(curr[:])
                return
            if rem<0 or idx>=len(candidates):
                return
            curr.append(candidates[idx])
            backtrack(idx,rem-candidates[idx],curr)
            curr.pop()
            backtrack(idx+1,rem,curr)
        backtrack(0,target,[])
        return res