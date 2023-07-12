class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join(map(str, digits))
        number = int(number) + 1
        return [int(x) for x in str(number)]