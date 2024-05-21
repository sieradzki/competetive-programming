class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        pattern_map = {char: None for char in set(pattern)}
        words = s.split()
        for i, char in enumerate(pattern):
            if pattern_map[char] is not None and pattern_map[char] != words[i]:
                return False
            elif pattern_map[char] is None:
                # check if this word already has a pattern char
                if words[i] in pattern_map.values():
                    return False
                pattern_map[char] = words[i]

        return True
