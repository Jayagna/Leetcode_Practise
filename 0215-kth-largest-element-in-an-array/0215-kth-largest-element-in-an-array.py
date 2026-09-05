from heapq import heappop,heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)-k+1
        heap = []

        for num in nums:
            heappush(heap,-num)
            if len(heap) > size:
                heappop(heap)

        return -heappop(heap)