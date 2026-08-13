class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()
        province = 0
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    adj_list[i].append(j)

        def dfs(city):
            if adj_list[city] == []:
                return
            visited.add(city)
            for neig in adj_list[city]:
                if neig not in visited:
                    dfs(neig)
            return

        for city in range(len(isConnected)):
            if city not in visited:
                province += 1
                dfs(city)

        return province
            