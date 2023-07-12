class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_dict = defaultdict(lambda: 0)

        for num in nums:
            n_dict[num] += 1

        srtd = list(sorted(n_dict.items(), key=lambda kv: kv[1], reverse=True))

        return [x[0] for x in srtd[:k]]