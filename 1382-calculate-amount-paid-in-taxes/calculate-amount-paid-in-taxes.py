class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res,prev = 0,0
        for val,perc in brackets:
            res += perc/100*min(val-prev,income)
            income -= val - prev
            prev = val
            if income <= 0:
                return res
