from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sort = sorted(freq.items() , key = lambda item: item[1], reverse = True)
        res = []
        for k,v in sort:
            for i in range(v):
                res.append(k)

        return ''.join(res)
