class StockPrice:

    def __init__(self):
        self.prices = {}

        self.latest = 0

        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        # Dictionary stores the REAL current price
        self.prices[timestamp] = price

        # Track largest timestamp
        self.latest = max(self.latest, timestamp)

        # Add new record to both heaps
        heapq.heappush(
            self.min_heap,
            (price, timestamp)
        )

        heapq.heappush(
            self.max_heap,
            (-price, timestamp)
        )

    def current(self) -> int:
        return self.prices[self.latest]

    def maximum(self) -> int:
        while self.max_heap:
            negative_price, timestamp = self.max_heap[0]

            price = -negative_price

            if self.prices[timestamp] == price:
                return price

            # stale record
            heapq.heappop(self.max_heap)

    def minimum(self) -> int:
        while self.min_heap:
            price, timestamp = self.min_heap[0]

            if self.prices[timestamp] == price:
                return price

            # stale record
            heapq.heappop(self.min_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()