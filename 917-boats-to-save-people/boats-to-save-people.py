class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        l,r = 0, len(people)-1
        
        while l <= r:
            if l == r:
                boats += 1
                break
            elif people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boats += 1
            else:
                boats += 1
                r -= 1
        return boats
        