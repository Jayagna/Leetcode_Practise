class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(arr,i,total):
            if total == target:
                res.append(arr.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            arr.append(candidates[i])
            dfs(arr,i+1,total+candidates[i])
            arr.pop()

            nexti = i+1
            while nexti < len(candidates) and candidates[i] == candidates[nexti]:
                nexti += 1 
            dfs(arr,nexti,total)

        dfs([],0,0)
        return res