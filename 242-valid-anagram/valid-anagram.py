class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)) :
            return False
        countT, countS = {} , {}
        for letter in s :
            countS[letter] = 1 + countS.get(letter,0)
        for letter in t : 
            countT[letter] = 1 + countT.get(letter,0)

        return countS == countT
        