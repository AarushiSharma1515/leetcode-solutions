class Solution(object):
    def groupAnagrams(self, strs):
        group = {}
        for s in strs:
            char = sorted(s) # -> ['a', 'e', 't']
            key = "".join(char) # -> "aet"

            if key in group:
                group[key].append(s)
            else:
                group[key]=[s]
        return list(group.values())
