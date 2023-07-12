class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            out = [i]
            req = target - num
            if req in nums:
                if nums.index(req) != i:
                    out.append(nums.index(req))
                    return out
                