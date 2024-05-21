class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {num: 0 for num in nums}
        for num in nums:
            nums_dict[num] += 1
        
        for key, val in nums_dict.items():
            if val > (len(nums) / 2):
                return key