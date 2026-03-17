class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0,len(numbers)-1
        while i<j:
            sums = numbers[i]+numbers[j]
            if sums == target:
                return [i+1,j+1]
            elif sums < target:
                i=i+1
            else:
                j=j-1
        