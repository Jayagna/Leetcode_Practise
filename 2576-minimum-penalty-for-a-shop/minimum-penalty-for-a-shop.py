class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        min_penalty = penalty
        res = 0

        for i in range(len(customers)):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                res = i + 1

        return res

        
        