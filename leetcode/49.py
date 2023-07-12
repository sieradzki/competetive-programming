class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            aux = "".join(sorted(s))
            anagrams[aux].append(s)
        return anagrams.values()