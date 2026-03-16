class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        w1 , w2 , res = 0,0, ''
        length = min(len(word1),len(word2))
        for w1 in range(length):
            res += word1[w1]
            res += word2[w2]
            w2 += 1
        w1 += 1
        
        while (w1 <= len(word1)-1):
            res += word1[w1]
            w1 += 1

        while (w2 <= len(word2)-1):
            res += word2[w2]
            w2 += 1
        
        return res
        