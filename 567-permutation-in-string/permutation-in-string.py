class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count_s1 = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1

        for l in range(len(s2) - len(s1) + 1):
            count_s2 = {}

            for i in range(l, l + len(s1)):
                count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1

            if count_s1 == count_s2:
                return True

        return False
        