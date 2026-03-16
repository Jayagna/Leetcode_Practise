class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j = 0,0
        result = ""
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1

        result += word1[i:]
        result += word2[j:]

        return result
        