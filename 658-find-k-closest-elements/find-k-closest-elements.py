class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr.append(x)
        arr.sort()

        for i in range(len(arr)):   
            if arr[i] == x:
                index = i
        
        l,r = index-1,index+1
        res = []

        length = 0
        while length < k:
            if r >= len(arr):
                res.append(arr[l])
                l -= 1
                length += 1
            
            elif l < 0:
                res.append(arr[r])
                r += 1
                length += 1
            
            elif ((arr[index] - arr[l]) > (arr[r] - arr[index])):
                res.append(arr[r])
                r += 1
                length += 1

            elif ((arr[index] - arr[l]) <= (arr[r] - arr[index])):
                res.append(arr[l])
                l -= 1
                length += 1
        
        res.sort()
        return res
        