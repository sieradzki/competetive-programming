class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = 0
        for i in range(len(min(strs, key=len))):
            if len(set([s[i] for s in strs])) == 1:
                prefix = i+1 # prefix is not inclusive
            else:
                break
                
        return strs[0][:prefix]