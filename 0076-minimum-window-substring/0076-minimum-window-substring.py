class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        res = ""
        tf = {}
        for char in t:
            tf[char] = 1 + tf.get(char,0)

        need = len(tf)
        have = 0

        l = 0
        sf = {}
        for r in range(len(s)):
            sf[s[r]] = 1 + sf.get(s[r],0)
            if s[r] in tf and sf[s[r]] == tf[s[r]]:
                have += 1

            while have == need:
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]

                    # Remove left character
                sf[s[l]] -= 1

                # Window becomes invalid
                if s[l] in tf and sf[s[l]] < tf[s[l]]:
                    have -= 1
                l += 1

        return res