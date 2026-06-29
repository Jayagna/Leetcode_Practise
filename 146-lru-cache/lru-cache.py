from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)  # remove old position
        self.cache[key] = value      # re-add at end = most recently used
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.pop(key)      # remove old position first

        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)  # remove least recently used

        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)