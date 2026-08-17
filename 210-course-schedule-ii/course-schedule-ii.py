class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adlist = defaultdict(list)
        for u,v in prerequisites:
            adlist[v].append(u)
            indegree[u] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
            
        topo = []
        while q:
            course = q.popleft()
            topo.append(course)
            for nei in adlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(topo) == numCourses:
            return topo
        return []