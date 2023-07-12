class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occs = {}
        for num in arr:
            if num in occs.keys():
                occs[num] += 1
            else:
                occs[num] = 1

        vals = occs.values()
        return len(vals) == len(set(vals))