class TimeMap:

    def __init__(self):
        self.nmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.nmap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l,r  = 0,len(self.nmap[key])-1
        res = -1
        while l <= r:
            mid = (r+l)//2
            if timestamp >= self.nmap[key][mid][1]:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        if res != -1:
            return self.nmap[key][res][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)