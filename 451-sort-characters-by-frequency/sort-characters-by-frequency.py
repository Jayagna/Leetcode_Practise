from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sort = freq.most_common()
        res = []
        for k,v in sort:
            for i in range(v):
                res.append(k)

        return ''.join(res)
