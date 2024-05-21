class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        used_chars = {c: -1 for c in ransomNote}
        for char in ransomNote:
            if char in magazine:
                if used_chars[char] == -1:
                    used_chars[char] = magazine.find(char)
                else:
                    if magazine.find(char, used_chars[char]+1) != -1:
                        used_chars[char] = magazine.find(char, used_chars[char]+1)
                    else:
                        return False
            else:
                return False
        return True

       