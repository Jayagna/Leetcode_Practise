class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for l,r in intervals: 
            if not merged or l > merged[-1][1]:
                merged.append([l,r])
            else:
                merged[-1][1] = max(merged[-1][1],r)

        return merged


