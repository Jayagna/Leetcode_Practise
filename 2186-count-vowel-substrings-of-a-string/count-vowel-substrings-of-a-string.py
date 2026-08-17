class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        for i in range(len(word)):
            for j in range(i + 4,len(word)):
                sub = set(word[i:j+1])
                if len(sub) == 5 and 'a' in sub and 'e' in sub and 'i' in sub and 'o' in sub and 'u' in sub:
                    cnt += 1
        return cnt