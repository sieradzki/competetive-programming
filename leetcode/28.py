class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i, letter in enumerate(haystack):
            if letter == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1

