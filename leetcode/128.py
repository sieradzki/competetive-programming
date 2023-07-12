class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        nums = sorted(list(set(nums)))

        length = 1
        max_len = 1
        prev = nums[0]
        for num in nums[1:]:
            if num - prev == 1:
                length += 1
                if length > max_len:
                    max_len = length
            else:
                length = 1
            prev = num
            
        return max_len
