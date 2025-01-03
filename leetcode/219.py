from collections import defaultdict


# I Beats ~8
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    indices = defaultdict(list)
    for i, num in enumerate(nums):  # O(n)
      indices[num].append(i)

    for key, vals in indices.items():  # O(n)
      if len(vals) > 1:
        for i, val1 in enumerate(vals):  # O(2)
          for j, val2 in enumerate(vals):
            if i != j and abs(val1 - val2) <= k:
              return True

    return False


# II # Beats 86.27
class Solution:
  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    if len(nums) == len(set(nums)):
      return False
    ws, we = 0, k + 1
    while True:
      if len(nums[ws:we]) != len(set(nums[ws:we])):
        return True
      if we >= len(nums):
        break
      ws += 1
      we += 1

    return False
