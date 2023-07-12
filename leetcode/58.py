class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        while not s[-1].isalnum():
            s.pop()
        return len(s[-1])