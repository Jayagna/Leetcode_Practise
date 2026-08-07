class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = {}

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(node, target, product, visited):
            if node == target:
                return product

            visited.add(node)

            for nei, weight in graph[node]:
                if nei not in visited:
                    ans = dfs(
                        nei,
                        target,
                        product * weight,
                        visited
                    )

                    if ans != -1:
                        return ans

            return -1

        res = []

        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(start, end, 1.0, set()))

        return res



        