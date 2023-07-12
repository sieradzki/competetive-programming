class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for word in s.split(' '):
            if word.isalnum():
                words.append(word)
        return ' '.join(words[::-1]).strip()