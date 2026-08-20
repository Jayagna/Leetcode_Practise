from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adlist = defaultdict(list)
        for u,v,dist in times:
            adlist[u-1].append([v-1,dist])
        
        distance = [float("inf")]*n
        heap = [(0,k-1)]
        distance[k-1] = 0

        while heap:
            dist,node = heappop(heap)
            if dist > distance[node]:
                continue
            for nei,wt in adlist[node]:
                curr = dist + wt
                if curr < distance[nei]:
                    distance[nei] = curr
                    heappush(heap,(curr,nei))

        if float("inf") in distance:
            return -1
        return max(distance)