class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        min_word = len(word1) if len(word1) < len(word2) else len(word2)

        for i in range(min_word):
            out += word1[i]
            out += word2[i]
        
        if len(word1) == min_word:
            out += word2[min_word:]
        else:
            out += word1[min_word:]
        
        return out