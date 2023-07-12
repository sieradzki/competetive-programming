class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(lambda: 0)

        for num in nums:
            counts[num] += 1

        srtd = list(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))
        return srtd[0][0]
