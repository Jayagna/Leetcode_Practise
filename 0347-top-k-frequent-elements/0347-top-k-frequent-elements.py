class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        res = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res