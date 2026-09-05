class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:

        if not self.heap1 and not self.heap2:
            self.heap1.append(-num)
            return

        if num > -self.heap1[0]:
            heapq.heappush(self.heap2,num)
            if abs(len(self.heap1) - len(self.heap2)) > 1:
                heapq.heappush(self.heap1,-heapq.heappop(self.heap2))

        else:
            heapq.heappush(self.heap1,-num)
            if abs(len(self.heap1) - len(self.heap2)) > 1:
                heapq.heappush(self.heap2,-heapq.heappop(self.heap1))

    def findMedian(self) -> float:
        cnt = len(self.heap1) + len(self.heap2)
        
        if cnt % 2 == 0:
            return (-self.heap1[0] + self.heap2[0]) / 2
        else:
            if len(self.heap1) > len(self.heap2):
                return -self.heap1[0]
            else:
                return self.heap2[0]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()