class Solution:
    def isPalindrome(self, s: str) -> bool:
        # define alphabet
        alphabet = [chr(x) for x in range(97, 97+26)] + [str(x) for x in range(0, 10)]

        # clean up the input string
        clean_s = ""
        for char in s.lower():
            if char in alphabet:
                clean_s += char
            
        for i, char in enumerate(clean_s[:len(clean_s)//2]):
            if char != clean_s[-(i+1)]:
                return False
        return True