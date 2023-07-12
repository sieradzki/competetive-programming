class Solution:
    def reverseVowels(self, s: str) -> str:
        vovels = ['a','e','i','o','u']
        backlog = []
        s = list(s)
        for c in s:
            if c.lower() in vovels:
                backlog.append(c)

        for i, c in enumerate(s[::-1]):
            if c.lower() in vovels:
                s[len(s)-1-i] = backlog.pop(0)
        
        return ''.join(s)