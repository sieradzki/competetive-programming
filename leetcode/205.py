class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def find_occurences(a_str, b_str):
            occurences = []
            start = 0
            while start <= len(b_str):
                occ = b_str.find(a_str, start)
                if occ != -1:
                    occurences.append(occ)
                    start += occ + len(a_str)
                else:
                    return occurences
            return occurences

        for i, char in enumerate(s):
            if find_occurences(char, s) != find_occurences(t[i], t):
                return False
        return True