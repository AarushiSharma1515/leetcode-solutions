class Solution(object):
    def longestConsecutive(self, nums):
        long_streak = 0
        hash_set = set(nums)
        for n in hash_set:
            if n-1 not in hash_set:
                curr = n
                curr_streak=1
                while curr+1 in hash_set:
                    curr+=1
                    curr_streak+=1
                long_streak = max(long_streak,curr_streak)
        return long_streak