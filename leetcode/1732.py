class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0
        for g in gain:
            alt += g
            if alt > max_alt:
                max_alt = alt
                
        return max_alt